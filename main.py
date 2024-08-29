from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class NewPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()

@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    all_post = result.scalars().all()
    posts = [{
        "id": post.id,
        "title": post.title,
        "subtitle": post.subtitle,
        "date": post.date,
        "body": post.body,
        "author": post.author,
        "img_url": post.img_url
    } for post in all_post]
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    result = db.session.execute(db.select(BlogPost).filter_by(id=post_id))
    requested_post = result.scalars().first()
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/new_post", methods=['GET', 'POST'])
def add_new_post():
    form = NewPost()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    else:
        print("Form Errors:", form.errors)  # Print form errors to the console
    return render_template("make-post.html", form=form)

@app.route("/edit/<int:post_id>", methods=['GET', 'POST'])
def edit(post_id):
    post = BlogPost.query.get_or_404(post_id)
    form = NewPost(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.img_url = form.img_url.data
        post.author = form.author.data
        post.body = form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=form, is_edit=True)

@app.route("/delete/<int:post_id>")
def delete(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

if __name__ == "__main__":
    app.run(debug=True, port=5003)

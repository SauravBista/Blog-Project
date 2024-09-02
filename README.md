Flask Blog Project

This is a Flask-based blog project where users can register, log in, create posts, comment on posts, and manage content. The project uses several Flask extensions like Flask-Bootstrap, Flask-CKEditor, Flask-Login, and more.
Table of Contents

    Features
    Installation
    Usage
    File Structure
    Database Models
    Routes
    Admin Only Features
    Contributing
    License

Features

    User registration and login with secure password hashing.
    Blog posts management: create, edit, and delete posts.
    Commenting system for authenticated users.
    Gravatar integration for user avatars.
    Admin-only routes for post management.
    Error handling and custom error pages.

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/flask-blog.git
cd flask-blog

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

On Windows:

venv\Scripts\activate

On MacOS/Linux:

bash

source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Set up the database:

python

flask shell
>>> from app import db
>>> db.create_all()
>>> exit()

Run the application:

arduino

    flask run

Usage

    Access the application in your web browser at http://localhost:5000/.
    Register a new user, or log in with an existing user account.
    Create, view, and comment on blog posts.
    Admin users can create, edit, and delete posts.

File Structure

graphql

flask-blog/
├── app.py                  # Main application file
├── forms.py                # Forms for user registration, login, post creation, etc.
├── templates/              # HTML templates for the views
│   ├── about.html
│   ├── contact.html
│   ├── error.html
│   ├── index.html
│   ├── login.html
│   ├── make-post.html
│   ├── post.html
│   ├── register.html
├── static/
│   ├── css/                # CSS files for styling
│   └── img/                # Image files
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation

Database Models

    User: Stores user information, including name, email, and hashed password. Users can have multiple posts and comments.
    BlogPost: Stores blog post details, including title, subtitle, body, image URL, and author.
    Comment: Stores comments associated with specific blog posts and users.

Routes

    /: Display all blog posts.
    /register: Register a new user.
    /login: Log in an existing user.
    /logout: Log out the current user.
    /new-post: Create a new blog post (Admin only).
    /edit-post/<int:post_id>: Edit an existing blog post (Admin only).
    /delete/<int:post_id>: Delete a blog post (Admin only).
    /post/<int:post_id>: View a specific blog post and add comments.
    /about: About page.
    /contact: Contact page.

Admin Only Features

The following routes are restricted to admin users (user ID = 1):

    Creating new posts
    Editing existing posts
    Deleting posts

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
License

This project is licensed under the MIT License. See the LICENSE file for details.

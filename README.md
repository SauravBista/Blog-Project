# Flask Blog Application

A simple blog application built using Flask, Flask-Bootstrap, Flask-SQLAlchemy, Flask-WTF, and Flask-CKEditor. This application allows users to create, edit, delete, and view blog posts with rich text content.

## Features

- **View All Posts**: Display a list of all blog posts on the homepage.
- **View Single Post**: Read individual blog posts.
- **Create New Post**: Add new blog posts with a title, subtitle, author, image URL, and rich text content.
- **Edit Post**: Modify existing blog posts.
- **Delete Post**: Remove blog posts from the application.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **Flask-Bootstrap**: Integrates Bootstrap 5 with Flask.
- **Flask-SQLAlchemy**: Adds SQLAlchemy support to Flask.
- **Flask-WTF**: Provides integration with WTForms for form handling.
- **Flask-CKEditor**: Adds CKEditor support for rich text editing.
- **SQLite**: Lightweight database used for storing blog posts.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

    Create and activate a virtual environment:

    bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:

bash

pip install -r requirements.txt

Create the database:

bash

python
>>> from app import db
>>> db.create_all()
>>> exit()

Run the application:

bash

    python app.py

    The application will start on http://localhost:5003.

Configuration

    SECRET_KEY: Set to '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'. Change this to a secure key in a production environment.
    SQLALCHEMY_DATABASE_URI: Points to an SQLite database file posts.db.

Routes

    / - Displays all blog posts.
    /post/<int:post_id> - Displays a single blog post.
    /about - About page.
    /contact - Contact page.
    /new_post - Form to create a new blog post.
    /edit/<int:post_id> - Form to edit an existing blog post.
    /delete/<int:post_id> - Delete a blog post.

Form Handling

    NewPost Form: Used for creating and editing blog posts. Includes fields for title, subtitle, author, image URL, and body.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Flask Documentation
    Flask-Bootstrap Documentation
    Flask-SQLAlchemy Documentation
    Flask-WTF Documentation
    Flask-CKEditor Documentation

Feel free to contribute to this project by creating issues or submitting pull requests.

arduino


You can replace placeholders like `https://github.com/yourusername/your-repository.git` with 

from flask import render_template
from app import app

posts = [
    {"title": "Welcome to My Blog", "content": "First post — hello world!", "author": "Steven"},
    {"title": "Why Flask?", "content": "Flask is light and nimble, perfect for quick projects.", "author": "Steven"}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)
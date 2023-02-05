from app import app
from flask import render_template, request, redirect, session


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/add-post')
def add_post():
    return render_template('add_post.html')

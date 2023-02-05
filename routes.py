from app import app
from flask import render_template, request, redirect, session
import users
from db import db


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':

        username = request.form['uname']
        password = request.form['psw']
        password2 = request.form['psw-repeat']
        if password != password2:
            return render_template('error.html', message="Passwords do not match", route="/register")
        if len(username) < 4:
            return render_template('error.html', message="Username must be at least 4 characters long", route="/register")
        if len(password) < 6:
            return render_template('error.html', message="Password must be at least 6 characters long", route="/register")
        if len(password) == 0:
            return render_template('error.html', message="Password cannot be empty", route="/register")
        if len(username) == 0:
            return render_template('error.html', message="Username cannot be empty", route="/register")

    if not users.register(username, password):
        return render_template('error.html', message="Rekisteröityminen ei onnistunut", route="/register")

    return redirect('/login')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/add-post')
def add_post():
    return render_template('add_post.html')

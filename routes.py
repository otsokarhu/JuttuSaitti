from app import app
from flask import render_template, request, redirect, session
import users
import topics
from db import db


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not users.login(username, password):
            return render_template('error.html', message="Väärä käyttäjätunnus tai salasana", route="/login")
        return redirect('/')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password-repeat']
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


@app.route('/categories', methods=['GET'])
def categories():
    categories = topics.get_categories()
    if request.method == 'GET':
        return render_template('categories.html', categories=categories)


@app.route('/category/<int:id>', methods=['GET', 'POST'])
def category(id):
    category = topics.get_category(id)
    if request.method == 'GET':
        return render_template('category.html', category=category)
    if request.method == 'POST':
        name = request.form['name']
        content = request.form['content']
        created_by = session['name']
        topics.add_topic(name, content, created_by, id)
        return redirect('/category/' + str(id))


@app.route('/category/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'GET':
        return render_template('add_category.html')
    if request.method == 'POST':
        name = request.form['name']
        topics.add_category(name)
        return redirect('/categories')


@app.route('/logout')
def logout():
    users.logout()
    return redirect('/')

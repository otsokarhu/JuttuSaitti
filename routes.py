from app import app
from flask import render_template, request, redirect, session
import users
import topics
import contacts
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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['subject']
        contacts.add_contact_request(name, email, message)
        return redirect('/')


@app.route('/contactrequests', methods=['GET'])
def contactrequests():
    if request.method == 'GET':
        contactrequests = contacts.get_contact_requests()
        return render_template('contact_requests.html', contact_requests=contactrequests)


@app.route('/categories', methods=['GET'])
def categories():
    categories = topics.get_categories()
    if request.method == 'GET':
        return render_template('categories.html', categories=categories)


@app.route('/category/<int:id>', methods=['GET', 'POST'])
def category(id):
    category = topics.get_category(id)
    alltopics = topics.get_topics(id)
    if request.method == 'GET':
        return render_template('category.html', category=category, topics=alltopics)
    if request.method == 'POST':
        name = request.form['title']
        content = request.form['content']
        created_by = session['user_id']
        category_id = id
        topics.add_topic(name, content, category_id, created_by)
        return redirect('/category/' + str(id))


@app.route('/category/<int:id>/delete', methods=['GET'])
def delete_category(id):
    topics.delete_category(id)
    return redirect('/categories')


@app.route('/category/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'GET':
        return render_template('add_category.html')
    if request.method == 'POST':
        name = request.form['name']
        topics.add_category(name)
        return redirect('/categories')


@app.route('/category/topic/<int:id>', methods=['GET', 'POST'])
def topic(id):
    topic = topics.get_topic(id)
    comments = topics.get_comments(id)
    if request.method == 'GET':
        return render_template('topic.html', topic=topic, comments=comments)
    if request.method == 'POST':
        content = request.form['content']
        created_by = session['user_id']
        topic_id = id
        topics.add_comment(content, topic_id, created_by)
        return redirect('/category/topic/' + str(id))


@app.route('/topic/<int:id>/comment/<int:comment_id>/delete', methods=['GET'])
def delete_comment(id, comment_id):
    topics.delete_comment(comment_id)
    return redirect('/category/topic/' + str(id))


@app.route('/category/topic/<int:id>/delete', methods=['GET'])
def delete_topic(id):
    topics.delete_topic(id)
    return redirect('/categories')


@app.route('/logout')
def logout():
    users.logout()
    return redirect('/')

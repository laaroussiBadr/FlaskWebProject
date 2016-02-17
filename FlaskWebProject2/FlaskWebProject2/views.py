"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, url_for
from FlaskWebProject2 import app
import redis

r = redis.StrictRedis(host='localhost',port=6379,db=0,charset='utf-8', decode_responses=True);

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/create', methods=['GET', 'POST'])
def create():
    """Renders the about page."""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        r.set(email, password)

        return render_template(
        'about.html',
        title=email,
        year=datetime.now().year,
        message='Your application description page.'
    )

    elif request.method == 'GET':
        return render_template(
            'create.html'
    )

@app.route('/users')
def users():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
        

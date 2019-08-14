from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index() :
    print(request)
    print(request.args)
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/user/<username>')
def user_profile(username):
    # show the user profile for that user
    return escape(f'User {username}')

@app.route('/post/<int:post_id>')
def post(post_id):
    # show the post with the given id, the id is an integer
    return escape(f'Post {post_id}')

@app.route('/path/<path:subpath>')
def path(subpath):
    # show the subpath after /path/
    return escape(f'Subpath {subpath}')

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about') # <---- different from /about/
def about():
    return 'The about page'

from flask import render_template, make_response

@app.route('/welcome/')
@app.route('/welcome/<name>')
def welcome(name = None):
    # can also just return render_template('welcome.html', name = name)
    resp = make_response(render_template('welcome.html', name = name))
    resp.set_cookie('name', name) # <-- you can access cookies from request.cookies
    return resp

from flask import url_for

with app.test_request_context():
    print("Got url for index :", url_for('index'))
    print("Got url for projects :", url_for('projects'))
    print("Got url for John : ", url_for('user_profile', username='John Doe'))

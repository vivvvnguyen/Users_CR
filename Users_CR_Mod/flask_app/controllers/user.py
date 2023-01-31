from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')
# Redirects to the Read All Page that displays all the data in the database
@app.route('/users')
def users():
    return render_template("read_all.html", users=User.get_all())
# Redirects to the create new (forms) page for user to input data
@app.route('/user/new')
def new():
    return render_template("create_new.html")
# Need to go back to the Read All Page where the newly added user should be displayed in the database
@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')
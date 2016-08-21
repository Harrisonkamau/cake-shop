from flask import Flask, g, render_template, redirect, flash, url_for, request
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import sqlite3
from models import DATABASE as db

import forms
import models

# create flask app
app = Flask(__name__)
# create a secret key
app.secret_key = 'auoesh.beoehgh.32.tibe.jeen'

# create a login manager
login_manager = LoginManager()
login_manager.init_app(app)  # sets up the login manager for the app
login_manager.login_view = 'login'


# load user route
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:  # exception got from peewee
        return None


# create a before request route
@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


# create an after request route
@app.after_request
def after_request(response):
    """Close the database after each request"""
    g.db.close()
    return response


# create a register route to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if not request.form['username']:
            error = 'You have to enter a username'
        elif not request.form['email'] or '@' not in request.form['email']:
            error = 'You have to enter a valid email address'
        elif not request.form['password']:
            error = 'You have to enter a password'
        else:
            print(request.form['username'])
            db.execute('INSERT INTO User VALUES (?, ?, ?)',
                       (request.form['username'], request.form['email'],
                        generate_password_hash(request.form['password'])))
            db.commit()
            flash('You were successfully registered and can login now')
            return render_template('layout.html')
    return render_template('register.html')


# create a login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.username == form.username.data)
        except models.DoesNotExist:
            flash("Your username and password do not match!", "error")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("Successfully logged in!!", "success")
                return redirect(url_for('home'))
            else:
                flash("Your emails and password do not match!", "error")
    return render_template('login.html', form=form)


# create a logout route
@login_required
@app.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out!", "success")
    return redirect(url_for('index'))


# use decorators to link the functions to the url
@app.route('/index')
def index():
    return render_template('home.html')


# create a home page
@app.route('/')
@login_required
def home():
    return render_template('layout.html')


# start the server
if __name__ == "__main__":
    models.initialize()
    try:
        models.User.create_user(
            username='harrisonkamau',
            email='kamauharry@yahoo.com',
            password='password',
            admin=True
        )
    except ValueError:
        pass
app.run(debug=True)

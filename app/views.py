from flask import Flask, g, render_template, redirect, flash, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
import os
from forms import RegistrationForm, LoginForm
import models


# create a flask Constructor
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# create a secret key
app.secret_key = os.urandom(24)

# disable SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cake.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


# create a login manager
login_manager = LoginManager()
login_manager.init_app(app)  # sets up the login manager for the app
login_manager.login_view = 'login'

# database object
db = SQLAlchemy(app)


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
    g.user = current_user
    if g.user.is_authenticated:
        db.session.add(g.user)
        db.session.commit()


# create a register route to register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = models.User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


# create a login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        login_user(user)
        return redirect(url_for('layout'))
    return render_template('login.html', form=form)


# create a logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out!", "success")
    return redirect('/login')


# create a home route
@app.route('/')
def index():
    return render_template('home.html')


# after logging in allow the user to make purchase
@app.route('/layout')
@login_required
def layout():
    return render_template('layout.html')


# create an error handler route
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


# start the server
if __name__ == "__main__":
    app.run(debug=True)


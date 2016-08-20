# import the Flask class from flask module
from flask import render_template, request, redirect, url_for, session
from app import app
from functools import wraps
import sqlite3
from flask_login import login_user, login_required
from forms import LoginForm
from models import User


# use  decorators to link a function to url
app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('layout'))
    return render_template('auth/login.html', form=form)



# logout route
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)  # pops out the True value of session and deletes the key(logged_in))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    # import ipdb; ipdb.set_trace()

    # validate the user's information against the defined Roles schema
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(name=request.form['username'], password=request.form['password'], email=request.form['email'])

        # automatically adds the user to the database(db)
        db.session.add(user)

        # save the changes to the db
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print "failed"

        # if registration is unsuccessful, render the registration form
    return render_template('register.html', form=form)


# catch errors
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

# connect to the application's db
def connect_db():
    return sqlite3.connect(app.database)


# start the server with the 'run()' method
# if __name__ == "__main__":
#     app.run(debug=True)

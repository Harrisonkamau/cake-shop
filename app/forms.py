from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp, Email, Length, EqualTo


# create a registration form
class RegistrationForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Username must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
                                                    DataRequired(),
                                                    EqualTo('confirm', message='Passwords must match.')])
    confirm = PasswordField('Repeat Password')


# create a login form
class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')





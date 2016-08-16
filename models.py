from flask_sqlalchemy import SQLAlchemy  # import SQAlchemy
from views import app  # import flask app from views module


# configure db
db = SQLAlchemy(app)


# create a users table
class User(db.Models):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    password = db.Column('password', db.String(250))
    first_name = db.Column('first name', db.String(50), unique=True, index=True)
    date_of_birth = db.Column('date of birth', db.DateTime)
    location  = db.Column('Location', db.String(50), unique=True, index=True)

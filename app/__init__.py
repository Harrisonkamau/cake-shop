from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
import config
from models import *

# set up flask app
app = Flask(__name__)


# connect to the database
sqlite3.connect(os.path.abspath("cake.db"))


# configure db uri
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cake.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# set a secret key to manage cookies/sessions
app.secret_key = os.urandom(40)


# instantiate db object
db = SQLAlchemy(app)

# start the server with run() method
# if __name__ == "__main__":
#     db.create_all()
#     x = User("test", "test@gmail.com","password")
#     db.session.add(x)
#     db.session.commit()
#
#     app.run(debug=True)

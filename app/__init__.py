from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# set up flask app
app = Flask(__name__)

# configure db uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/cake.db'


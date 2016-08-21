# import modules

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *


# set up database
DATABASE = SqliteDatabase('cake.db')


# create a users' model
class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)

    class Meta:
        database = DATABASE

    @classmethod  # without this, a user instance has to be created to call create_user to create a user instance!
    def create_user(cls, username, email, password, admin=False):
        try:  # cls refers to the User class
            with DATABASE.transaction():
                cls.create(
                    username=username,
                    email=email,
                    password=generate_password_hash(password)
                           )

        except IntegrityError:
            raise ValueError("User already exists!")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# initialize migration
migrate = Migrate(app, db)

# manage migrations
manager = Manager(app)

manager.add_command('db', MigrateCommand)


# start the migration
if __name__ == "__main__":
    manager.run()



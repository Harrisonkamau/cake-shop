# import Flask class from flask module
from flask import Flask, render_template, request, redirect, url_for, abort, session

# create flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'hialreuhsan.ndjfbfhgfhfhfre'


# use decorators to link the functions to the url
@app.route('/index')
def index():
    return render_template('index.html')


# create a home page
@app.route('/')
def home():
    return render_template('layout.html')

# start the server
if __name__ == "__main__":
    app.run(debug=True)

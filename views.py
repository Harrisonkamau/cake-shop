# import Flask class from flask module
from flask import Flask, render_template

# create flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'F34TF$($e34D';


# use decorators to link the functions to the url
@app.route('/index')
def index():
    return render_template('index.html')


# start the server
if __name__ == "__main__":
    app.run(debug=True)

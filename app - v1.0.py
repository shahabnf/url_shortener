from flask import Flask     # import flask library to our project

app = Flask(__name__)       # create a flask app

# print(__name__)

@app.route('/')             # redirect or route for home page OR '/'
def home():                 # Define a new function for our code
    return 'Hello Flask!'   # print or return string


@app.route('/about')                    # redirect or route for home page OR '/'
def about():                            # Define a new function for our code
    return 'This is a url shortener.'   # print or return string
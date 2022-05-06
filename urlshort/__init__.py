from flask import Flask

def create_app(test_config=None):       # test
    app = Flask(__name__)       # create a flask app
    app.secret_key = 'sfgb35+w65rgjfbhjbg/*w^dg'        # use secret key to communicate with user securely
    # print(__name__)

    from . import urlshort
    app.register_blueprint(urlshort.bp)     #register into application

    return app
import pytest
from urlshort import create_app     # import function from our project

@pytest.fixture             # use fixture to establish testing situation
def app():                  # function app
    app = create_app()      #
    yield app

@pytest.fixture
def client(app):            # function client , app as parameter
    return app.test_client()    # print out test result
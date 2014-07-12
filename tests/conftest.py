from flask import Flask
from flask.ext.statics import Statics
import pytest


@pytest.fixture(autouse=True, scope='session')
def app_context(request):
    """Initialize the Flask application for tests."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    Statics(app)
    context = app.app_context()
    context.push()
    request.addfinalizer(lambda: context.pop())

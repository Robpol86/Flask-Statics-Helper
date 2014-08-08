import re

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


@pytest.fixture(scope='session')
def template():
    """Load template example in README.md."""
    regex = re.compile(r'```html\+django\n(.*)```', re.DOTALL)
    file_path = 'README.md'
    with open(file_path) as f:
        t = re.findall(regex, f.read())[0]
    return t

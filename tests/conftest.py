import re

from flask import Flask
from flask.ext.statics import ALL_RESOURCES, ALL_RESOURCES_MINIFIED, Statics
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


@pytest.fixture(scope='session')
def all_files_both():
    """Get a set of all files for non-minified and minified resources."""
    all_files = set([f for r in ALL_RESOURCES.values() for f in r['css'] + r['js']])
    all_files_minified = set([f for r in ALL_RESOURCES_MINIFIED.values() for f in r['css'] + r['js']])
    return all_files, all_files_minified

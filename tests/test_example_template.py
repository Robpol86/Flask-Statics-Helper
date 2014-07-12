import re

from flask import current_app, render_template_string
import pytest


@pytest.fixture(scope='session')
def template():
    """Load template example in README.md."""
    regex = re.compile(r'```html\+django\n(.*)```', re.DOTALL)
    file_path = 'README.md'
    with open(file_path) as f:
        template = re.findall(regex, f.read())[0]
    return template


def test_template(template):
    with current_app.app_context():
        html = render_template_string(template).splitlines()

    assert 2 == len([i for i in html if '<link' in i])
    assert 2 == len([i for i in html if '<script' in i])

    relevant = ''.join([i for i in html if '<link' in i or '<script' in i])
    assert 'bootstrap' in relevant
    assert 'jquery' in relevant
    assert 'csshake' in relevant

    assert '<!DOCTYPE html>' in html
    assert '<html>' in html
    assert '<body>' in html
    assert '</body>' in html
    assert '</html>' in html

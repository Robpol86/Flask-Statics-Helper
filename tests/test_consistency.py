import os
import re
from string import Template

from flask import Flask, render_template_string
import pytest

from flask.ext.statics import ABS_STATIC_ROOT, ALL_VARIABLES, Statics


def test_files_exist(all_files_both):
    all_files, all_files_minified = all_files_both

    assert any(all_files)
    assert any(all_files_minified)

    for f in all_files:
        assert os.path.isfile(os.path.join(ABS_STATIC_ROOT, f))

    for f in all_files_minified:
        assert os.path.isfile(os.path.join(ABS_STATIC_ROOT, f))


@pytest.mark.parametrize('minify', (False, True))
def test_files_reachable_from_template(minify):
    # Define variables.
    re_find_css = re.compile(r'<link rel="stylesheet" href="/static/flask_statics_helper/(.*?)">')
    re_find_js = re.compile(r'<script src="/static/flask_statics_helper/(.*?)"></script>')
    template_base = Template("""
        {% extends 'flask_statics_helper/base.html' %}
        {% set STATICS_ENABLE_RESOURCE_$name = True %}
        {% block title %}Test Template{% endblock %}
    """)
    local_file = lambda x: os.path.join(ABS_STATIC_ROOT, x)
    remote_file = lambda x: '/static/flask_statics_helper/{0}'.format(x)

    # Create Flask app.
    app = Flask(__name__ + str(minify))
    app.config['STATICS_MINIFY'] = minify
    Statics(app)
    all_resources = ((k, set(v['css']), set(v['js']))
                     for k, v in app.extensions['statics'].statics.all_resources.items())
    assert minify == app.config['STATICS_MINIFY']

    # Test.
    for name, css_files, js_files in all_resources:
        # Get template HTML.
        template = template_base.substitute(name=name)
        with app.app_context():
            html = render_template_string(template)
        assert '<title>Test Template</title>' in html

        # Make sure all resources are mentioned.
        found_css = set(re_find_css.findall(html))
        found_js = set(re_find_js.findall(html))
        assert found_css == set(css_files)
        assert found_js == set(js_files)

        # Make sure resources are reachable.
        with app.test_client() as c:
            for resource in found_css | found_js:
                data_remote = c.get(remote_file(resource)).data
                with open(local_file(resource)) as f:
                    assert data_remote == f.read()


def test_documented():
    with open('README.md') as f:
        readme = f.read()
    for name in ALL_VARIABLES:
        assert '`STATICS_ENABLE_RESOURCE_{0}`'.format(name) in readme

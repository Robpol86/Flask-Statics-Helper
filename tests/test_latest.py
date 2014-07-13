"""Test for latest versions of certain static resources."""

from distutils.version import LooseVersion
import json
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen  # PY3

from flask_statics.resource_definitions import ResourceBootstrap, ResourceFontAwesome, ResourceJQuery


def download(url):
    response = urlopen(url)
    payload = response.read().decode('utf-8')
    data = json.loads(payload)
    return data


def test_bootstrap():
    current_version = ResourceBootstrap.DIR.split('-')[-1]
    url = 'https://api.github.com/repos/twbs/bootstrap/releases'
    data = download(url)
    all_versions = [r['name'].lower()[1:] for r in data]
    versions = sorted([v for v in all_versions if 'rc' not in v and 'beta' not in v], key=LooseVersion)
    latest_version = versions[-1]
    assert current_version == latest_version


def test_jquery():
    current_version = ResourceJQuery.DIR.split('-')[-1]
    url = 'https://api.github.com/repos/jquery/jquery/tags'
    data = download(url)
    all_versions = [r['name'].lower() for r in data]
    versions = sorted([v for v in all_versions if 'rc' not in v and 'beta' not in v], key=LooseVersion)
    latest_version = versions[-1]
    assert current_version == latest_version


def test_font_awesome():
    current_version = ResourceFontAwesome.DIR.split('-')[-1]
    url = 'https://api.github.com/repos/FortAwesome/Font-Awesome/tags'
    data = download(url)
    all_versions = [r['name'].lower()[1:] for r in data]
    versions = sorted([v for v in all_versions if 'rc' not in v and 'beta' not in v], key=LooseVersion)
    latest_version = versions[-1]
    assert current_version == latest_version

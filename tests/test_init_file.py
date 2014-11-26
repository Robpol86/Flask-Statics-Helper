import os

from flask import current_app, Flask
import pytest

from flask.ext.statics import Statics


class FakeApp(object):
    config = dict()
    static_url_path = ''

    def register_blueprint(self, _):
        pass


def test_minify():
    app = Flask(__name__)
    statics = Statics()
    statics.init_app(app)
    assert False == app.config['STATICS_MINIFY']

    all_files = set([f for r in statics.all_resources.values() for f in r['css'] + r['js']])
    assert 0 == len([f for f in all_files if '.min.' in f])
    assert 27 == len(all_files)

    app = Flask(__name__)
    app.config['STATICS_MINIFY'] = True
    statics = Statics()
    statics.init_app(app)
    assert True == app.config['STATICS_MINIFY']

    all_files = set([f for r in statics.all_resources.values() for f in r['css'] + r['js']])
    assert 22 == len([f for f in all_files if '.min.' in f])
    assert 27 == len(all_files)


def test_blueprint():
    statics = current_app.extensions['statics'].statics
    assert current_app.blueprints['flask_statics_helper'] == statics.blueprint

    expected_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    expected_static_path = os.path.join(expected_root, 'flask_statics', 'static')
    actual_static_path = statics.blueprint.static_folder

    assert expected_static_path == actual_static_path


def test_order():
    statics = current_app.extensions['statics'].statics
    pos_jquery = statics.all_variables.index('JQUERY')
    pos_bootstrap = statics.all_variables.index('BOOTSTRAP')

    assert pos_jquery < pos_bootstrap


def test_multiple():
    assert 'statics' in current_app.extensions

    with pytest.raises(ValueError):
        Statics(current_app)


def test_one_dumb_line():
    app = FakeApp()
    Statics(app)
    assert 'statics' in app.extensions

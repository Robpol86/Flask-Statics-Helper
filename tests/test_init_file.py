import os

from flask import current_app, Flask
from flask.ext.statics import Statics


def test_minify():
    app = Flask(__name__)
    statics = Statics()
    statics.init_app(app)
    assert False == app.config['STATICS_MINIFY']

    all_files = set([f for r in statics.all_resources.values() for f in r['css'] + r['js']])
    assert 0 == len([f for f in all_files if '.min.' in f])
    assert 25 == len(all_files)

    app = Flask(__name__)
    app.config['STATICS_MINIFY'] = True
    statics = Statics()
    statics.init_app(app)
    assert True == app.config['STATICS_MINIFY']

    all_files = set([f for r in statics.all_resources.values() for f in r['css'] + r['js']])
    assert 20 == len([f for f in all_files if '.min.' in f])
    assert 25 == len(all_files)


def test_blueprint():
    statics = current_app.extensions['statics'].statics
    assert current_app.blueprints['flask_statics_helper'] == statics.blueprint

    expected_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    actual_static_path = statics.blueprint.static_folder

    assert os.path.join(expected_root, 'flask_statics', 'static') == actual_static_path


def test_order():
    statics = current_app.extensions['statics'].statics
    pos_jquery = statics.all_variables.index('JQUERY')
    pos_bootstrap = statics.all_variables.index('BOOTSTRAP')

    assert pos_jquery < pos_bootstrap

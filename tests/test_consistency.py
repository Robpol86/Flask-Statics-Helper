import os

from flask import current_app
from flask.ext.statics import ABS_STATIC_ROOT


def test_files_exist(all_files_both):
    all_files, all_files_minified = all_files_both

    assert any(all_files)
    assert any(all_files_minified)

    for f in all_files:
        assert os.path.isfile(os.path.join(ABS_STATIC_ROOT, f))

    for f in all_files_minified:
        assert os.path.isfile(os.path.join(ABS_STATIC_ROOT, f))


def test_files_reachable_from_template():
    all_resources = ((k, v['css'], v['js']) for k, v in current_app.extensions['statics'].statics.all_resources.items())
    assert False == current_app.config['STATICS_MINIFY']

    for name, css_files, js_files in all_resources:
        pass
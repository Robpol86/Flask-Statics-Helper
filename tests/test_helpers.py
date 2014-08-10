from flask_statics.helpers import get_resources, priority


def test_priority():
    values = ['CSSHAKE', 'BOOTSTRAP', 'ANGULAR', 'JQUERY']
    values.sort(key=priority)
    assert ['JQUERY', 'BOOTSTRAP', 'ANGULAR', 'CSSHAKE'] == values


def test_get_resources(all_files_both):
    all_resources = get_resources()
    all_resources_minified = get_resources(minify=True)
    assert all_resources.keys() == all_resources_minified.keys()
    assert all_resources.values() != all_resources_minified.values()

    all_files, all_files_minified = all_files_both
    assert all('.min.' not in f for f in all_files)
    assert any('.min.' in f for f in all_files_minified)

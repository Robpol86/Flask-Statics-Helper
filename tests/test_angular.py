from flask import current_app, render_template_string


def test_normal():
    template = """
    {% extends 'flask_statics_helper/base.html' %}
    {% set STATICS_ENABLE_RESOURCE_ANGULARJS_MOCKS = True %}
    """

    with current_app.app_context():
        html = [l.strip() for l in render_template_string(template).splitlines()]

    angular = [i for i in html if i.startswith('<script') and i.endswith('angular.js"></script>')]
    angular_mocks = [i for i in html if i.startswith('<script') and i.endswith('angular-mocks.js"></script>')]
    assert 1 == len(angular)
    assert 1 == len(angular_mocks)

    angular_pos = html.index(angular[0])
    angular_mocks_pos = html.index(angular_mocks[0])
    assert angular_pos < angular_mocks_pos


def test_duplicates():
    template = """
    {% extends 'flask_statics_helper/base.html' %}
    {% set STATICS_ENABLE_RESOURCE_ANGULARJS_MOCKS = True %}
    {% set STATICS_ENABLE_RESOURCE_ANGULARJS_COOKIES = True %}
    """

    with current_app.app_context():
        html = [l.strip() for l in render_template_string(template).splitlines()]

    angular = [i for i in html if i.startswith('<script') and i.endswith('angular.js"></script>')]
    angular_mocks = [i for i in html if i.startswith('<script') and i.endswith('angular-mocks.js"></script>')]
    angular_cookies = [i for i in html if i.startswith('<script') and i.endswith('angular-cookies.js"></script>')]
    assert 1 == len(angular)
    assert 1 == len(angular_mocks)
    assert 1 == len(angular_cookies)

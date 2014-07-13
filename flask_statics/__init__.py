"""Provides Bootstrap3 and other static resources in a modular fashion.

https://github.com/Robpol86/Flask-Statics-Helper
https://pypi.python.org/pypi/Flask-Statics-Helper
"""

from flask import Blueprint

import resource_base
import resource_definitions
import resource_definitions_angular

__author__ = '@Robpol86'
__license__ = 'MIT'
__version__ = '0.1.1'


def priority(var):
    """Prioritizes resource position in the final HTML. To be fed into sorted(key=).

    Javascript consoles throw errors if Bootstrap's js file is mentioned before jQuery. Using this function such errors
    can be avoided. Used internally.

    Positional arguments:
    var -- value sent by list.sorted(), which is a value in Statics().all_variables.

    Returns:
    Either a number if sorting is enforced for the value in `var`, or returns `var` itself.
    """
    order = dict(JQUERY=0, BOOTSTRAP=1)
    return order.get(var, var)


class _StaticsState(object):
    """Remembers the configuration for the (statics, app) tuple. Modeled from SQLAlchemy."""

    def __init__(self, statics, app):
        self.statics = statics
        self.app = app


class Statics(object):
    """Static css/js resources for Flask applications.

    Relevant configuration settings from the Flask app config:
    STATICS_MINIFY -- set to True to have minified resources selected instead of uncompressed resources.

    Optional settings to enable specific static resources on all templates by default instead of on-demand:
    STATICS_ENABLE_RESOURCE_<resource name> -- refer to resource_definitions.py for list of options. Set to True to
        enable everywhere.
    """

    def __init__(self, app=None):
        self.all_variables = list()
        self.all_resources = dict()
        self.blueprint = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the extension."""
        # Set default Flask config option.
        app.config.setdefault('STATICS_MINIFY', False)

        # Populate resources
        subclasses = resource_base.ResourceBase.__subclasses__() + resource_definitions.ResourceAngular.__subclasses__()
        for resource in subclasses:
            obj = resource(app)
            self.all_resources[resource.RESOURCE_NAME] = dict(css=tuple(obj.resources_css), js=tuple(obj.resources_js))
        self.all_variables = sorted(self.all_resources.keys(), key=priority)

        # Add this instance to app.extensions.
        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        app.extensions['statics'] = _StaticsState(self, app)

        # Initialize blueprint.
        name = 'flask_statics_helper'
        static_url_path = '{0}/{1}'.format(app.static_url_path, name)
        self.blueprint = Blueprint(name, __name__, template_folder='templates', static_folder='static',
                static_url_path=static_url_path)
        self.blueprint.add_app_template_global(self.all_variables, '_flask_statics_helper_all_variables')
        self.blueprint.add_app_template_global(self.all_resources, '_flask_statics_helper_all_resources')
        app.register_blueprint(self.blueprint)

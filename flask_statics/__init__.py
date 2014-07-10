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
__version__ = '0.1.0'


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
            self.all_variables.append(resource.RESOURCE_NAME)
            obj = resource(app)
            self.all_resources[resource.RESOURCE_NAME] = dict(css=tuple(obj.resources_css), js=tuple(obj.resources_js))

        # Add this instance to app.extensions.
        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        app.extensions['statics'] = _StaticsState(self, app)

        # Initialize blueprint.
        name = 'flask_statics_helper'
        static_url_path = '{}/{}'.format(app.static_url_path, name)
        self.blueprint = Blueprint(name, __name__, template_folder='templates', static_folder='static',
                static_url_path=static_url_path)
        self.blueprint.add_app_template_global(self.all_resources, '_flask_statics_helper_all_resources')
        app.register_blueprint(self.blueprint)

"""Provides Bootstrap3 and other static resources in a modular fashion.

Adding new resources requires editing three files (besides tests):
    resource_definitions.py
    macros.html
    README.md

https://github.com/Robpol86/Flask-Statics-Helper
https://pypi.python.org/pypi/Flask-Statics-Helper
"""

import os

from flask import Blueprint

from flask_statics import resource_base
from flask_statics import resource_definitions
from flask_statics import resource_definitions_angular
from flask_statics.helpers import get_resources, priority

__author__ = '@Robpol86'
__license__ = 'MIT'
__version__ = '0.3.0'
ABS_STATIC_ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
ALL_RESOURCES = get_resources(minify=False)
ALL_VARIABLES = sorted(ALL_RESOURCES.keys(), key=priority)
ALL_RESOURCES_MINIFIED = get_resources(minify=True)


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
        self.all_variables = None
        self.all_resources = None
        self.blueprint = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the extension."""
        # Set default Flask config option.
        app.config.setdefault('STATICS_MINIFY', False)

        # Select resources.
        self.all_resources = ALL_RESOURCES_MINIFIED if app.config.get('STATICS_MINIFY') else ALL_RESOURCES
        self.all_variables = ALL_VARIABLES

        # Add this instance to app.extensions.
        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        if 'statics' in app.extensions:
            raise ValueError('Already registered extension STATICS.')
        app.extensions['statics'] = _StaticsState(self, app)

        # Initialize blueprint.
        name = 'flask_statics_helper'
        static_url_path = '{0}/{1}'.format(app.static_url_path, name)
        self.blueprint = Blueprint(name, __name__, template_folder='templates', static_folder='static',
                                   static_url_path=static_url_path)
        self.blueprint.add_app_template_global(self.all_variables, '_flask_statics_helper_all_variables')
        self.blueprint.add_app_template_global(self.all_resources, '_flask_statics_helper_all_resources')
        app.register_blueprint(self.blueprint)

"""Provides Bootstrap3 and other static resources in a modular fashion.

https://github.com/Robpol86/Flask-Statics-Helper
https://pypi.python.org/pypi/Flask-Statics-Helper
"""

from urlparse import urljoin

from flask import Blueprint
from jinja2 import Environment, FileSystemLoader

import resource_base
import resource_definitions

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
        # Set default Flask config options.
        app.config.setdefault('STATICS_MINIFY', False)
        for resource in resource_base.ResourceBase.__subclasses__():
            app.config.setdefault(resource.TEMPLATE_FLAG, False)

        # Populate resources
        for resource in resource_base.ResourceBase.__subclasses__():
            self.all_variables.append(resource.TEMPLATE_FLAG)
            obj = resource(app)
            self.all_resources[resource.TEMPLATE_FLAG] = dict(css=obj.resources_css, js=obj.resources_js)

        # Add this instance to app.extensions.
        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        app.extensions['statics'] = _StaticsState(self, app)

        # Initialize blueprint.
        name = 'flask_statics'
        self.blueprint = Blueprint(name, __name__, template_folder='templates', static_folder='static',
                static_url_path=urljoin(app.static_url_path, name))
        app.register_blueprint(self.blueprint)

        # Expose data to this extension's templates folder.
        env = Environment(loader=FileSystemLoader(self.blueprint.template_folder))
        env.globals.update(
            dict(flask_statics_all_variables=self.all_variables, flask_statics_all_resources=self.all_resources)
        )

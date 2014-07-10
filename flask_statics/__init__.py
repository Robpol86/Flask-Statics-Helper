"""Provides Bootstrap3 and other static resources in a modular fashion.

https://github.com/Robpol86/Flask-Statics-Helper
https://pypi.python.org/pypi/Flask-Statics-Helper
"""

from urlparse import urljoin

from flask import Blueprint

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
    STATICS_PSEUDO_URL_PREFIX -- in case of conflicts for some reason, override the default URL prefix used internally.

    Optional settings to enable specific static resources on all templates by default instead of on-demand:
    STATICS_ENABLE_RESOURCE_<resource name> -- refer to resource_definitions.py for list of options. Set to True to
        enable everywhere.
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the extension."""
        # Set default Flask config options.
        app.config.setdefault('STATICS_MINIFY', False)
        app.config.setdefault('STATICS_PSEUDO_URL_PREFIX', '_flask_statics_')
        for resource in resource_base.ResourceBase.__subclasses__():
            app.config.setdefault(resource.TEMPLATE_FLAG, False)

        # Add this instance to app.extensions.
        if not hasattr(app, 'extensions'):
            app.extensions = dict()
        app.extensions['statics'] = _StaticsState(self, app)

        # Populate resources
        all_variables = list()
        all_resources = dict()
        for resource in resource_base.ResourceBase.__subclasses__():
            all_variables.append(resource.TEMPLATE_FLAG)
            obj = resource(app)
            all_resources[resource.TEMPLATE_FLAG] = dict(css=obj.resources_css, js=obj.resources_js)
        setattr(app.g, 'flask_statics_helper_variables', all_variables)
        setattr(app.g, 'flask_statics_helper_resources', all_resources)

        # Initialize blueprint.
        name = app.config['STATICS_PSEUDO_URL_PREFIX']
        bp = Blueprint(name, __name__, template_folder='templates', static_folder='static',
                       static_url_path=urljoin(app.static_url_path, name))
        app.register_blueprint(bp)

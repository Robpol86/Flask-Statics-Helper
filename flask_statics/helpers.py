"""Helper functions for Flask-Statics."""

from flask_statics import resource_base
from flask_statics import resource_definitions


def priority(var):
    """Prioritizes resource position in the final HTML. To be fed into sorted(key=).

    Javascript consoles throw errors if Bootstrap's js file is mentioned before jQuery. Using this function such errors
    can be avoided. Used internally.

    Positional arguments:
    var -- value sent by list.sorted(), which is a value in Statics().all_variables.

    Returns:
    Either a number if sorting is enforced for the value in `var`, or returns `var` itself.
    """
    order = dict(JQUERY='0', BOOTSTRAP='1')
    return order.get(var, var)


def get_resources(minify=False):
    """Find all resources which subclass ResourceBase.

    Keyword arguments:
    minify -- select minified resources if available.

    Returns:
    Dictionary of available resources. Keys are resource names (part of the config variable names), values are dicts
    with css and js keys, and tuples of resources as values.
    """
    all_resources = dict()
    subclasses = resource_base.ResourceBase.__subclasses__() + resource_definitions.ResourceAngular.__subclasses__()
    for resource in subclasses:
        obj = resource(minify)
        all_resources[resource.RESOURCE_NAME] = dict(css=tuple(obj.resources_css), js=tuple(obj.resources_js))
    return all_resources

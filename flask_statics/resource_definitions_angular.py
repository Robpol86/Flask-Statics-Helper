"""Holds defined resources for AngularJS, subclassing resource_base.ResourceBase."""

from resource_definitions import ResourceAngular


class ResourceAngularAnimate(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_ANIMATE'

    def __init__(self, app):
        super(ResourceAngularAnimate, self).__init__(app)
        self.add_js('', 'angular-animate')


class ResourceAngularCookies(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_COOKIES'

    def __init__(self, app):
        super(ResourceAngularCookies, self).__init__(app)
        self.add_js('', 'angular-cookies')


class ResourceAngularCsp(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_CSP'

    def __init__(self, app):
        super(ResourceAngularCsp, self).__init__(app)
        self.add_css('', 'angular-csp')


class ResourceAngularLoader(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_LOADER'

    def __init__(self, app):
        super(ResourceAngularLoader, self).__init__(app)
        self.add_js('', 'angular-loader')


class ResourceAngularMessages(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_MESSAGES'

    def __init__(self, app):
        super(ResourceAngularMessages, self).__init__(app)
        self.add_js('', 'angular-messages')


class ResourceAngularMocks(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_MOCKS'

    def __init__(self, app):
        super(ResourceAngularMocks, self).__init__(app)
        self.add_js('', 'angular-mocks')


class ResourceAngularResource(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_RESOURCE'

    def __init__(self, app):
        super(ResourceAngularResource, self).__init__(app)
        self.add_js('', 'angular-resource')


class ResourceAngularRoute(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_ROUTE'

    def __init__(self, app):
        super(ResourceAngularRoute, self).__init__(app)
        self.add_js('', 'angular-route')


class ResourceAngularSanitize(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_SANITIZE'

    def __init__(self, app):
        super(ResourceAngularSanitize, self).__init__(app)
        self.add_js('', 'angular-sanitize')


class ResourceAngularScenario(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_SCENARIO'

    def __init__(self, app):
        super(ResourceAngularScenario, self).__init__(app)
        self.add_js('', 'angular-scenario')


class ResourceAngularTouch(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_TOUCH'

    def __init__(self, app):
        super(ResourceAngularTouch, self).__init__(app)
        self.add_js('', 'angular-touch')

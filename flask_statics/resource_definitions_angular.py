"""Holds defined resources for AngularJS, subclassing resource_base.ResourceBase."""

from flask_statics.resource_definitions import ResourceAngular


class ResourceAngularAnimate(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_ANIMATE'

    def __init__(self, minify):
        super(ResourceAngularAnimate, self).__init__(minify)
        self.add_js('', 'angular-animate')


class ResourceAngularCookies(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_COOKIES'

    def __init__(self, minify):
        super(ResourceAngularCookies, self).__init__(minify)
        self.add_js('', 'angular-cookies')


class ResourceAngularCsp(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_CSP'

    def __init__(self, minify):
        super(ResourceAngularCsp, self).__init__(minify)
        self.add_css('', 'angular-csp')


class ResourceAngularLoader(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_LOADER'

    def __init__(self, minify):
        super(ResourceAngularLoader, self).__init__(minify)
        self.add_js('', 'angular-loader')


class ResourceAngularMessages(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_MESSAGES'

    def __init__(self, minify):
        super(ResourceAngularMessages, self).__init__(minify)
        self.add_js('', 'angular-messages')


class ResourceAngularMocks(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_MOCKS'

    def __init__(self, minify):
        super(ResourceAngularMocks, self).__init__(minify)
        self.add_js('', 'angular-mocks')


class ResourceAngularResource(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_RESOURCE'

    def __init__(self, minify):
        super(ResourceAngularResource, self).__init__(minify)
        self.add_js('', 'angular-resource')


class ResourceAngularRoute(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_ROUTE'

    def __init__(self, minify):
        super(ResourceAngularRoute, self).__init__(minify)
        self.add_js('', 'angular-route')


class ResourceAngularSanitize(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_SANITIZE'

    def __init__(self, minify):
        super(ResourceAngularSanitize, self).__init__(minify)
        self.add_js('', 'angular-sanitize')


class ResourceAngularScenario(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_SCENARIO'

    def __init__(self, minify):
        super(ResourceAngularScenario, self).__init__(minify)
        self.add_js('', 'angular-scenario')


class ResourceAngularTouch(ResourceAngular):
    RESOURCE_NAME = 'ANGULARJS_TOUCH'

    def __init__(self, minify):
        super(ResourceAngularTouch, self).__init__(minify)
        self.add_js('', 'angular-touch')

"""Holds defined resources, subclassing resource_base.ResourceBase."""

from flask_statics.resource_base import ResourceBase


class ResourceJQuery(ResourceBase):
    DIR = 'jquery'
    RESOURCE_NAME = 'JQUERY'

    def __init__(self, minify):
        super(ResourceJQuery, self).__init__(minify)
        self.add_js('', 'jquery-2.1.1')


class ResourceAngular(ResourceBase):
    DIR = 'angular'
    RESOURCE_NAME = 'ANGULARJS'

    def __init__(self, minify):
        super(ResourceAngular, self).__init__(minify)
        self.add_js('', 'angular')


class ResourceBootstrap(ResourceBase):
    DIR = 'bootstrap'
    RESOURCE_NAME = 'BOOTSTRAP'

    def __init__(self, minify):
        super(ResourceBootstrap, self).__init__(minify)
        self.add_css('css', 'bootstrap')
        self.add_js('js', 'bootstrap')


class ResourceBootstrapEditable(ResourceBase):
    DIR = 'bootstrap3-editable'
    RESOURCE_NAME = 'BOOTSTRAP_EDITABLE'

    def __init__(self, minify):
        super(ResourceBootstrapEditable, self).__init__(minify)
        self.add_css('css', 'bootstrap-editable')
        self.add_js('js', 'bootstrap-editable')


class ResourceBootstrapGrowl(ResourceBase):
    DIR = 'bootstrap-growl'
    RESOURCE_NAME = 'BOOTSTRAP_GROWL'

    def __init__(self, minify):
        super(ResourceBootstrapGrowl, self).__init__(minify)
        self.add_js('', 'bootstrap-growl')


class ResourceBootstrapTypeahead(ResourceBase):
    DIR = 'typeahead'
    RESOURCE_NAME = 'BOOTSTRAP_TYPEAHEAD'

    def __init__(self, minify):
        super(ResourceBootstrapTypeahead, self).__init__(minify)
        self.add_js('', 'typeahead.bundle')


class ResourceBootstrapValidator(ResourceBase):
    DIR = 'BootstrapValidator'
    RESOURCE_NAME = 'BOOTSTRAP_VALIDATOR'

    def __init__(self, minify):
        super(ResourceBootstrapValidator, self).__init__(minify)
        self.add_css('css', 'bootstrapValidator')
        self.add_js('js', 'bootstrapValidator')


class ResourceCSShake(ResourceBase):
    DIR = 'csshake'
    RESOURCE_NAME = 'CSSHAKE'

    def __init__(self, minify):
        super(ResourceCSShake, self).__init__(minify)
        self.add_css('', 'csshake')


class ResourceD3(ResourceBase):
    DIR = 'd3'
    RESOURCE_NAME = 'D3'

    def __init__(self, minify):
        super(ResourceD3, self).__init__(minify)
        self.add_js('', 'd3')


class ResourceDataTables(ResourceBase):
    DIR = 'DataTables'
    RESOURCE_NAME = 'DATATABLES'

    def __init__(self, minify):
        super(ResourceDataTables, self).__init__(minify)
        self.add_css('css', 'jquery.dataTables')
        self.add_js('js', 'jquery.dataTables')


class ResourceFontAwesome(ResourceBase):
    DIR = 'font-awesome'
    RESOURCE_NAME = 'FONT_AWESOME'

    def __init__(self, minify):
        super(ResourceFontAwesome, self).__init__(minify)
        self.add_css('css', 'font-awesome')


class ResourceWHHGFont(ResourceBase):
    DIR = 'whhg-font'
    RESOURCE_NAME = 'WHHG_FONT'

    def __init__(self, minify):
        super(ResourceWHHGFont, self).__init__(minify)
        self.add_css('css', 'whhg')

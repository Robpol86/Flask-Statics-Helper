"""Holds defined resources, subclassing resource_base.ResourceBase."""

from resource_base import ResourceBase


class ResourceAngular(ResourceBase):
    DIR = 'angular-1.3.0-beta.14'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('ANGULARJS')

    def __init__(self, app):
        super(ResourceAngular, self).__init__(app)
        self.add_js('', 'angular')


class ResourceBootstrap(ResourceBase):
    DIR = 'bootstrap-3.2.0'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('BOOTSTRAP')

    def __init__(self, app):
        super(ResourceBootstrap, self).__init__(app)
        self.add_css('css', 'bootstrap')
        self.add_js('js', 'bootstrap')


class ResourceBootstrapEditable(ResourceBase):
    DIR = 'bootstrap3-editable-1.5.1'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('BOOTSTRAP_EDITABLE')

    def __init__(self, app):
        super(ResourceBootstrapEditable, self).__init__(app)
        self.add_css('css', 'bootstrap-editable')
        self.add_js('js', 'bootstrap-editable')


class ResourceBootstrapGrowl(ResourceBase):
    DIR = 'bootstrap-growl-2.0.0'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('BOOTSTRAP_GROWL')

    def __init__(self, app):
        super(ResourceBootstrapGrowl, self).__init__(app)
        self.add_js('', 'bootstrap-growl')


class ResourceBootstrapTypeahead(ResourceBase):
    DIR = 'Bootstrap-3-Typeahead-3.0.3'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('BOOTSTRAP_TYPEAHEAD')

    def __init__(self, app):
        super(ResourceBootstrapTypeahead, self).__init__(app)
        self.add_js('', 'bootstrap3-typeahead')


class ResourceCSShake(ResourceBase):
    DIR = 'csshake-20140709'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('CSSHAKE')

    def __init__(self, app):
        super(ResourceCSShake, self).__init__(app)
        self.add_css('', 'csshake')


class ResourceD3(ResourceBase):
    DIR = 'd3-3.4.9'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('D3')

    def __init__(self, app):
        super(ResourceD3, self).__init__(app)
        self.add_js('', 'd3')


class ResourceDataTables(ResourceBase):
    DIR = 'DataTables-1.10.0'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('DATATABLES')

    def __init__(self, app):
        super(ResourceDataTables, self).__init__(app)
        self.add_css('css', 'jquery.dataTables')
        self.add_js('js', 'jquery.dataTables')


class ResourceFontAwesome(ResourceBase):
    DIR = 'font-awesome-4.1.0'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('FONT_AWESOME')

    def __init__(self, app):
        super(ResourceFontAwesome, self).__init__(app)
        self.add_css('css', 'font-awesome')


class ResourceJQuery(ResourceBase):
    DIR = 'jquery-2.1.1'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('JQUERY')

    def __init__(self, app):
        super(ResourceJQuery, self).__init__(app)
        self.add_js('', 'jquery-2.1.1')


class ResourceWHHGFont(ResourceBase):
    DIR = 'whhg-font-20140709'
    TEMPLATE_FLAG = ResourceBase.TEMPLATE_FLAG.format('WHHG_FONT')

    def __init__(self, app):
        super(ResourceWHHGFont, self).__init__(app)
        self.add_css('css', 'whhg')

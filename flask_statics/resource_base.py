"""Holds the base Resource class."""

import os


class ResourceBase(object):
    """Base class for loading resources (such as DataTables or Bootstrap).

    Class variables:
    DIR -- directory name under the static folder where files for this static resource reside.
    RESOURCE_NAME -- variable to set to True inside a template that wishes to use this resource (subclassing this
        class).

    Instance variables:
    minify -- Used to determine if minified resources should be selected in <link /> and <script /> tags or if developer
        non-minified resources should be selected instead. Default is non-minified.
    resources_css -- list of css files associated with this static resource.
    resources_js -- list of js files.
    """
    DIR = ''
    STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
    RESOURCE_NAME = ''

    def __init__(self, minify):
        self.minify = minify
        self.resources_css = list()
        self.resources_js = list()

    def file_exists(self, subdir, prefix, suffix):
        """Returns true if the resource file exists, else False.

        Positional arguments:
        subdir -- sub directory name under the resource's main directory (e.g. css or js, or an empty string if the
            resource's directory structure is flat).
        prefix -- file name without the file extension.
        suffix -- file extension (if self.minify = True, includes .min before the extension).
        """
        real_path = os.path.join(self.STATIC_DIR, self.DIR, subdir, prefix + suffix)
        return os.path.exists(real_path)

    def add_css(self, subdir, file_name_prefix):
        """Add a css file for this resource.

        If self.minify is True, checks if the .min.css file exists. If not, falls back to non-minified file. If that
        file also doesn't exist, IOError is raised.

        Positional arguments:
        subdir -- sub directory name under the resource's main directory (e.g. css or js, or an empty string).
        file_name_prefix -- file name without the file extension.
        """
        suffix_maxify = '.css'
        suffix_minify = '.min.css'
        if self.minify and self.file_exists(subdir, file_name_prefix, suffix_minify):
            self.resources_css.append(os.path.join(self.DIR, subdir, file_name_prefix + suffix_minify))
        elif self.file_exists(subdir, file_name_prefix, suffix_maxify):
            self.resources_css.append(os.path.join(self.DIR, subdir, file_name_prefix + suffix_maxify))
        else:
            file_path = os.path.join(self.STATIC_DIR, self.DIR, subdir, file_name_prefix + suffix_maxify)
            raise IOError('Resource file not found: {0}'.format(file_path))

    def add_js(self, subdir, file_name_prefix):
        """Same as self.add_css() but for js files."""
        suffix_maxify = '.js'
        suffix_minify = '.min.js'
        if self.minify and self.file_exists(subdir, file_name_prefix, suffix_minify):
            self.resources_js.append(os.path.join(self.DIR, subdir, file_name_prefix + suffix_minify))
        elif self.file_exists(subdir, file_name_prefix, suffix_maxify):
            self.resources_js.append(os.path.join(self.DIR, subdir, file_name_prefix + suffix_maxify))
        else:
            file_path = os.path.join(self.STATIC_DIR, self.DIR, subdir, file_name_prefix + suffix_maxify)
            raise IOError('Resource file not found: {0}'.format(file_path))

from flask.ext.statics.resource_base import ResourceBase
import pytest


def test_add_methods():
    resource = ResourceBase(False)

    with pytest.raises(IOError):
        resource.add_css('', 'dne')

    with pytest.raises(IOError):
        resource.add_js('', 'dne')

from unittest import TestCase

from assertpy import assert_that

from gen.app.factories.template_factory import TemplateFactory
from gen.app.factories.wawi_uri_factory import WaWiUriFactory
from gen.model.template import Template
from gen.model.template_type import TemplateType
from gen.utils import values


class TestTemplateFactory(TestCase):
    def test_create_crud(self):
        uri_fac = WaWiUriFactory(values.default_base_uri)
        fac = TemplateFactory(TemplateType.CRUD, values.default_base_uri)
        default_replacers = values.default_replacers("ProductElementPrice", "ERP")
        expected = [
            Template(uri_fac.controller("ERP", "ProductElementPrice")[0],
                     uri_fac.controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.i_controller("ERP", "ProductElementPrice")[0],
                     uri_fac.i_controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.test_controller("ERP", "ProductElementPrice")[0],
                     uri_fac.test_controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.repo("ERP", "ProductElementPrice")[0],
                     uri_fac.repo("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.i_repo("ERP", "ProductElementPrice")[0],
                     uri_fac.i_repo("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.test_repository("ERP", "ProductElementPrice")[0],
                     uri_fac.test_repository("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.api_controller("ERP", "ProductElementPrice")[0],
                     uri_fac.api_controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.test_api_controller("ERP", "ProductElementPrice")[0],
                     uri_fac.test_api_controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
        ]
        assert_that(fac.create("ERP", "ProductElementPrice")).is_equal_to(expected)

    def test_create_searchable(self):
        uri_fac = WaWiUriFactory(values.default_base_uri)
        fac = TemplateFactory(TemplateType.SEARCHABLE, values.default_base_uri)
        default_replacers = values.default_replacers("ProductElementPrice", "ERP")
        expected = [
            Template(uri_fac.searchable_controller("ERP", "ProductElementPrice")[0],
                     uri_fac.searchable_controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.i_searchable_controller("ERP", "ProductElementPrice")[0],
                     uri_fac.i_searchable_controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.test_controller("ERP", "ProductElementPrice")[0],
                     uri_fac.test_controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.searchable_repo("ERP", "ProductElementPrice")[0],
                     uri_fac.searchable_repo("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.i_searchable_repo("ERP", "ProductElementPrice")[0],
                     uri_fac.i_searchable_repo("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.test_repository("ERP", "ProductElementPrice")[0],
                     uri_fac.test_repository("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.searchable_api_controller("ERP", "ProductElementPrice")[0],
                     uri_fac.searchable_api_controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
            Template(uri_fac.test_api_controller("ERP", "ProductElementPrice")[0],
                     uri_fac.test_api_controller("ERP", "ProductElementPrice")[1],
                     default_replacers),
        ]
        result = fac.create("ERP", "ProductElementPrice")
        for i, j in zip(expected, result):
            assert_that(i).is_equal_to(j)

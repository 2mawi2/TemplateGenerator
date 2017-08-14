from unittest import TestCase

from assertpy import assert_that

from gen.application.factories.wawi_uri_factory import WaWiUriFactory
from gen.utils import values


class TestFilename(TestCase):
    def test_controller(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.controller("CRM", "Customer")
        expected = f"{values.default_base_uri}CRM\\Controllers\\CustomerController.cs"
        assert_that(uri).is_equal_to(expected)

    def test_i_controller(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.i_controller("CRM", "Customer")
        expected = f"{values.default_base_uri}CRM\\ICustomerController.cs"
        assert_that(uri).is_equal_to(expected)

    def test_repo(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.repo("CRM", "Customer")
        expected = f"{values.default_base_uri}PersistenceCRM\\Repositories\\CustomerRepository.cs"
        assert_that(uri).is_equal_to(expected)

    def test_i_repo(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.i_repo("CRM", "Customer")
        expected = f"{values.default_base_uri}PersistenceCRM\\ICustomerRepository.cs"
        assert_that(uri).is_equal_to(expected)

    def test_api_controller(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.api_controller("CRM", "Customer")
        expected = f"{values.default_base_uri}AdminApi\\Controllers\\CRM\\CustomerApiController.cs"
        assert_that(uri).is_equal_to(expected)

    def test_test_controller(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.test_controller("CRM", "Customer")
        expected = f"{values.default_base_uri}Tests\\CRM\\CRM\\Controllers\\CustomerControllerTests.cs"
        assert_that(uri).is_equal_to(expected)

    def test_test_api_controller(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.test_api_controller("CRM", "Customer")
        expected = f"{values.default_base_uri}Tests\\Api\\AdminApi\\CRM\\CustomerApiControllerTests.cs"
        assert_that(uri).is_equal_to(expected)

    def test_test_repository(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.test_repository("CRM", "Customer")
        expected = f"{values.default_base_uri}Tests\\CRM\\PersistenceCRM\\Repositories\\CustomerRepositoryTests.cs"
        assert_that(uri).is_equal_to(expected)

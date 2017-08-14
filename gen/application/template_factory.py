from gen.application.template_type import TemplateType
from gen.application.wawi_uri_factory import WaWiUriFactory
from gen.file_generator.template import Template
from gen.utils import values


class TemplateFactory:
    def __init__(self,
                 template_type,
                 base_path,
                 replacers: dict = None) -> None:
        self.replacers = replacers
        self.base_path = base_path
        self.template_type = template_type
        self.fac = WaWiUriFactory(self.base_path)

    def create(self, package_name, entity_name) -> [Template]:
        if self.replacers is None:
            self.replacers = values.default_replacers(entity_name, package_name)
        if self.template_type is TemplateType.CRUD:
            return self.__create_crud_templates(package_name, entity_name)
        elif self.template_type is TemplateType.SEARCHABLE:
            return self.__create_searchable_templates(package_name, entity_name)

    def __create_crud_templates(self, package_name, entity_name) -> [Template]:
        return self.__generate_templates(package_name, entity_name, [
            (values.crud_controller_template, self.fac.controller),
            (values.icrud_controller_template, self.fac.i_controller),
            (values.test_controller_template, self.fac.test_controller),
            (values.crud_repository_template, self.fac.repo),
            (values.icrud_repository_template, self.fac.i_repo),
            (values.test_repository_template, self.fac.test_repository),
            (values.crud_api_controller_template, self.fac.api_controller),
            (values.test_api_controller_template, self.fac.test_api_controller),
        ])

    def __create_searchable_templates(self, package_name, entity_name) -> [Template]:
        return self.__generate_templates(package_name, entity_name, [
            (values.searchable_controller_template, self.fac.controller),
            (values.isearchable_controller_template, self.fac.i_controller),
            (values.test_controller_template, self.fac.test_controller),
            (values.searchable_repository_template, self.fac.repo),
            (values.isearchable_repository_template, self.fac.i_repo),
            (values.test_repository_template, self.fac.test_repository),
            (values.searchable_api_controller_template, self.fac.api_controller),
            (values.test_api_controller_template, self.fac.test_api_controller),
        ])

    def __generate_templates(self, package_name: str, entity_name: str, template_output_tuple_list: [(str,)]):
        return [Template(t, o(package_name, entity_name), self.replacers) for t, o in template_output_tuple_list]

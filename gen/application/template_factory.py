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

    def create(self, package_name, entity_name) -> [Template]:
        if self.replacers is None:
            self.replacers = values.default_replacers(entity_name, package_name)
        if self.template_type is TemplateType.CRUD:
            return self.__create_crud_templates(package_name, entity_name)
        elif self.template_type is TemplateType.SEARCHABLE:
            return self.__create_searchable_templates(package_name, entity_name)

    def __create_crud_templates(self, package_name, entity_name) -> [Template]:
        fac = WaWiUriFactory(self.base_path)
        templates = [
            Template(values.crud_controller_template,
                     fac.controller(package_name, entity_name),
                     self.replacers),
            Template(values.icrud_controller_template,
                     fac.i_controller(package_name, entity_name),
                     self.replacers),
            Template(values.crud_repository_template,
                     fac.repo(package_name, entity_name),
                     self.replacers),
            Template(values.icrud_repository_template,
                     fac.i_repo(package_name, entity_name),
                     self.replacers),
            Template(values.crud_api_controller_template,
                     fac.admin_api_controller(entity_name),
                     self.replacers),
        ]
        return templates

    def __create_searchable_templates(self, package_name, entity_name) -> [Template]:
        fac = WaWiUriFactory(self.base_path)
        templates = [
            Template(values.searchable_controller_template,
                     fac.controller(package_name, entity_name),
                     self.replacers),
            Template(values.isearchable_controller_template,
                     fac.i_controller(package_name, entity_name),
                     self.replacers),
            Template(values.searchable_repository_template,
                     fac.repo(package_name, entity_name),
                     self.replacers),
            Template(values.isearchable_repository_template,
                     fac.i_repo(package_name, entity_name),
                     self.replacers),
            Template(values.searchable_api_controller_template,
                     fac.admin_api_controller(entity_name),
                     self.replacers),
        ]
        return templates
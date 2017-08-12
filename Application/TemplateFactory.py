from Application import Templates
from Application.TemplateType import TemplateType
from Application.WaWiUriFactory import WaWiUriFactory
from FileGenerator.Template import Template
from Utils import Values


class TemplateFactory:
    def __init__(self, template_type, base_path) -> None:
        self.base_path = base_path
        self.template_type = template_type

    def create(self, package_name, entity_name) -> [Template]:
        if self.template_type is TemplateType.CRUD:
            return self.__create_crud_templates(package_name, entity_name)
        elif self.template_type is TemplateType.SEARCHABLE:
            return self.__create_searchable_templates(package_name, entity_name)

    def __create_crud_templates(self, package_name, entity_name) -> [Template]:
        fac = WaWiUriFactory(self.base_path)
        dr = Values.default_replacers
        templates = [
            Template(Templates.crud_controller_template,
                     fac.controller(package_name, entity_name),
                     dr(entity_name, package_name)),
            Template(Templates.icrud_controller_template,
                     fac.i_controller(package_name, entity_name),
                     dr(entity_name, package_name)),
            Template(Templates.crud_repository_template,
                     fac.repo(package_name, entity_name),
                     dr(entity_name, package_name)),
            Template(Templates.icrud_repository_template,
                     fac.i_repo(package_name, entity_name),
                     dr(entity_name, package_name)),
            Template(Templates.crud_api_controller_template,
                     fac.admin_api_controller(entity_name),
                     dr(entity_name, package_name)),
        ]
        return templates

    def __create_searchable_templates(self, package_name, entity_name) -> [Template]:
        fac = WaWiUriFactory(self.base_path)
        dr = Values.default_replacers
        templates = [
            Template(Templates.searchable_controller_template,
                     fac.controller(package_name, entity_name),
                     dr(entity_name, package_name)),
            Template(Templates.isearchable_controller_template,
                     fac.i_controller(package_name, entity_name),
                     dr(entity_name, package_name)),
            Template(Templates.searchable_repository_template,
                     fac.repo(package_name, entity_name),
                     dr(entity_name, package_name)),
            Template(Templates.isearchable_repository_template,
                     fac.i_repo(package_name, entity_name),
                     dr(entity_name, package_name)),
            Template(Templates.searchable_api_controller_template,
                     fac.admin_api_controller(entity_name),
                     dr(entity_name, package_name)),
        ]
        return templates

from Application import WaWiUriFactory, Templates
from Application.TemplateType import TemplateType
from Generator.Template import Template


class TemplateFactory:
    def __init__(self, template_type) -> None:
        self.template_type = template_type

    def create(self, package_name, entity_name) -> [Template]:
        if self.template_type is TemplateType.CRUD:
            return self.__create_crud_templates(package_name, entity_name)
        elif self.template_type is TemplateType.SEARCHABLE:
            return self.__create_searchable_templates(package_name, entity_name)

    def __create_crud_templates(self, package_name, entity_name) -> [Template]:
        fac = WaWiUriFactory
        templates = [
            Template(Templates.crud_controller_template,
                     WaWiUriFactory.controller(package_name, entity_name),
                     Template.default_replacers(entity_name, package_name)),
            Template(Templates.icrud_controller_template,
                     WaWiUriFactory.i_controller(package_name, entity_name),
                     Template.default_replacers(entity_name, package_name)),
            Template(Templates.crud_repository_template,
                     WaWiUriFactory.repo(package_name, entity_name),
                     Template.default_replacers(entity_name, package_name)),
            Template(Templates.icrud_repository_template,
                     WaWiUriFactory.i_repo(package_name, entity_name),
                     Template.default_replacers(entity_name, package_name)),
            Template(Templates.crud_api_controller_template,
                     WaWiUriFactory.admin_api_controller(entity_name),
                     Template.default_replacers(entity_name, package_name)),
        ]
        return templates

    def __create_searchable_templates(self, package_name, entity_name) -> [Template]:
        pass

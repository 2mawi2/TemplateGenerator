from Application import WaWiUriFactory, Templates
from Application.TemplateType import TemplateType
from Generator.Template import Template


class TemplateFactory:
    def create(self, t: TemplateType) -> [Template]:
        if t is TemplateType.CRUD:
            pass

    def __create_crud_templates(self) -> [Template]:
        fac = WaWiUriFactory
        c = fac.controller("ERP", "ProductElementPrice")
        ic = fac.i_controller("ERP", "ProductElementPrice")
        apicon = fac.i_controller("ERP", "ProductElementPrice")
        template = Template(Templates.)

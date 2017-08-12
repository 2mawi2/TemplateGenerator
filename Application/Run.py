from Application import WaWiUriFactory
from Generator.Generator import Generator
from Generator.Template import Template


def make_templates():
    fac = WaWiUriFactory
    c = fac.controller("ERP", "ProductElementPrice")
    ic = fac.i_controller("ERP", "ProductElementPrice")
    apicon = fac.i_controller("ERP", "ProductElementPrice")
    template = Template()


generator = Generator(make_templates())
generator.generate()

from Application.TemplateFactory import TemplateFactory
from Application.TemplateType import TemplateType
from Generator.Generator import Generator

templateFactory = TemplateFactory(TemplateType.CRUD)
templates = templateFactory.create("ERP", "ProductElementPrice")

generator = Generator(templates)
generator.generate()

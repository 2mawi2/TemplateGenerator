from Application.TemplateFactory import TemplateFactory
from Application.TemplateType import TemplateType
from FileGenerator.FileGenerator import FileGenerator
from Utils import Values

templateFactory = TemplateFactory(TemplateType.SEARCHABLE, Values.default_base_uri)
templates = templateFactory.create("CRM", "ProductElementPrice")

generator = FileGenerator(templates)
generator.generate()

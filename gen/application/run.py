from gen.application.template_factory import TemplateFactory
from gen.application.template_type import TemplateType
from gen.file_generator.file_generator import FileGenerator
from gen.utils import values

templateFactory = TemplateFactory(TemplateType.SEARCHABLE, values.default_base_uri)
templates = templateFactory.create("CRM", "ProductElementPrice")

generator = FileGenerator(templates)
generator.generate()

from gen.application.factories.template_factory import TemplateFactory
from gen.file_generator.file_generator import FileGenerator
from gen.model.template_type import TemplateType
from gen.utils import values

templateFactory = TemplateFactory(TemplateType.SEARCHABLE, values.default_base_uri)
templates = templateFactory.create("ERP", "ProductElementPrice")

generator = FileGenerator(templates)
generator.generate()

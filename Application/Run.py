from Application.TemplateFactory import TemplateFactory
from Application.TemplateType import TemplateType

templateFactory = TemplateFactory(TemplateType.CRUD)
templates = templateFactory.create("ERP", "ProductElementPrice")
print(templates)

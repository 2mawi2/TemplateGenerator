from generator.FileIO import FileIO
from generator.Template import Template


class Generator:
    def __init__(self, template: Template):
        self.template = template

    def generate(self):
        uri = self.template.template_uri
        name = self.template.template_name
        output = self.template.output_uri
        if not FileIO.exists(uri):
            return
        self.replace_placeholder(name, output, uri)

    @staticmethod
    def replace_placeholder(name, output, uri):
        content = FileIO.read(uri)
        content = content.replace("###", name)
        FileIO.write(output, content)

from Generator.FileIO import FileIO
from Generator.Template import Template


class Generator:
    def __init__(self, templates: [Template]):
        self.templates = templates

    def generate(self):
        for t in self.templates:
            uri = t.template_uri
            name = t.template_name
            output = t.output_uri
            if not FileIO.exists(uri) or not name:
                return
            self.create_file_from_template(name, output, uri)

    @staticmethod
    def create_file_from_template(name, output, uri):
        content = FileIO.read(uri)
        content = content.replace("###", name)
        FileIO.write(output, content)

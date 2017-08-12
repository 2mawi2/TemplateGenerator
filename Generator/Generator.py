from Generator.FileIO import FileIO
from Generator.Template import Template


class Generator:
    def __init__(self, templates: [Template]):
        self.templates = templates

    def generate(self):
        for t in self.templates:
            if not FileIO.exists(t.template_uri) or not t.template_name or FileIO.exists(t.output_uri):
                return
            self.__create_file_from_template(t.template_name, t.package, t.output_uri, t.template_uri)

    @staticmethod
    def __create_file_from_template(name, package, output, uri):
        content = FileIO.read(uri)
        content = content.replace("<#name#>", name)
        content = content.replace("<#package#>", package)
        content = content.replace("<#packageLC#>", str.lower(package))
        FileIO.write(output, content)

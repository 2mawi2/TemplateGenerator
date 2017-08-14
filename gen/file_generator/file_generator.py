from gen.file_generator.file_io import FileIO
from gen.model.template import Template


class FileGenerator:
    def __init__(self, templates: [Template]):
        self.templates = templates

    def generate(self) -> None:
        for t in self.templates:
            self.__validate_template(t)
            self.__create_file_from_template(t)
            print(f"generated template: {t.template_uri} in directory: {t.output_uri}")

    @staticmethod
    def __validate_template(t: Template) -> None:
        if not FileIO.exists(t.template_uri):
            raise FileNotFoundError(f"no such template: {t.template_uri}")
        if FileIO.exists(t.output_uri):
            raise FileExistsError(f"template: {t.output_uri} already exsists")

    @staticmethod
    def __create_file_from_template(t: Template) -> None:
        content = FileIO.read(t.template_uri)
        for key, value in t.replacers.items():
            content = content.replace(key, value)
        FileIO.write(t.output_uri, content)

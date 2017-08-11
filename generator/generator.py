class Template:
    def __init__(self,
                 template_uri: str = None,
                 template_name: str = None):
        self.template_uri = template_uri
        self.template_name = template_name


class Generator:
    def __init__(self, template: Template):
        self.template = template

    def generate(self):
        if self.template is not None:
            return True

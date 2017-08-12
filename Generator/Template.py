class Template:
    def __init__(self,
                 template_uri: str,
                 output_uri: str,
                 replacers: dict):
        self.template_uri = template_uri
        self.output_uri = output_uri
        self.replacers = replacers

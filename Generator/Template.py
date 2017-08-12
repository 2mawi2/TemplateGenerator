class Template:
    def __init__(self,
                 template_uri: str,
                 output_uri: str,
                 template_name: str,
                 package: str):
        self.package = package
        self.template_name = template_name
        self.output_uri = output_uri
        self.template_uri = template_uri

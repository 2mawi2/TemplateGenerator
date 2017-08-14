class Template:
    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.__dict__ == o.__dict__
        return False

    def __init__(self,
                 template_uri: str,
                 output_uri: str,
                 replacers: dict):
        self.template_uri = template_uri
        self.output_uri = output_uri
        self.replacers = replacers

    def __str__(self) -> str:
        return f"{self.template_uri}, {self.output_uri}, {self.replacers}"

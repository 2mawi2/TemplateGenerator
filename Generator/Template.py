from Utils import StringUtils


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

    @staticmethod
    def default_replacers(entity_name, package_name):
        return {
            "<#name#>": StringUtils.upper_first_letter(entity_name),
            "<#package#>": str.upper(package_name),
            "<#packageLC#>": str.lower(package_name),
            "<#packageFLUC#>": str.capitalize(package_name)
        }

class WaWiUriFactory:
    def __init__(self, base_uri) -> None:
        self.base_uri = base_uri

    def controller(self, project, name):
        return f'{self.base_uri}{project}\\Controllers\\{self.filename(name, "Controller")}'

    def i_controller(self, project, name):
        return f'{self.base_uri}{project}\\I{self.filename(name, "Controller")}'

    def repo(self, project, name):
        return f'{self.base_uri}Persistence{project}\\Repositories\\{self.filename(name, "Repository")}'

    def i_repo(self, project, name):
        return f'{self.base_uri}Persistence{project}\\I{self.filename(name, "Repository")}'

    def admin_api_controller(self, name):
        return f'{self.base_uri}AdminApi\\Controllers\\CRM\\{self.filename(name, "ApiController")}'

    def filename(self, name, postfix):
        return f"{name}{postfix}.cs"

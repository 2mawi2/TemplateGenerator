class WaWiUriFactory:
    def __init__(self, base_uri) -> None:
        self.base_uri = base_uri

    def controller(self, project, name):
        return f'{self.base_uri}{project}\\Controllers\\{self.filename(name, "Controller")}'

    def i_controller(self, project, name):
        return f'{self.base_uri}{project}\\I{self.filename(name, "Controller")}'

    def test_controller(self, project, name):
        return f'{self.base_uri}Tests\\{project}\\{project}\\Controllers\\{self.filename(name, "ControllerTests")}'

    def repo(self, project, name):
        return f'{self.base_uri}Persistence{project}\\Repositories\\{self.filename(name, "Repository")}'

    def i_repo(self, project, name):
        return f'{self.base_uri}Persistence{project}\\I{self.filename(name, "Repository")}'

    def api_controller(self, project, name):
        return f'{self.base_uri}AdminApi\\Controllers\\{project}\\{self.filename(name, "ApiController")}'

    def test_api_controller(self, project, name):
        return f'{self.base_uri}Tests\\Api\\AdminApi\\{project}\\{self.filename(name, "ApiControllerTests")}'

    def test_repository(self, project, name):
        return f'{self.base_uri}Tests\\{project}\\Persistence{project}\\Repositories\\' \
               f'{self.filename(name, "RepositoryTests")}'

    def filename(self, name, postfix):
        return f"{name}{postfix}.cs"

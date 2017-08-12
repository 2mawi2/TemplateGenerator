output_uri = "..\\Content\ExampleRepository.cs"
example_template_uri = "..\\Content\ExampleTemplate.cs"

base_uri = "C:\\Users\\Marius\\Source\\Repos\\WaWi_Backend\\"


def controller(project, name):
    return f'{base_uri}{project}\\Controllers\\{filename(name, "Controller")}'


def i_controller(project, name):
    return f'{base_uri}{project}\\I{filename(name, "Controller")}'


def repo(project, name):
    return f'{base_uri}Persistence{project}\\Repositories\\{filename(name, "Repository")}'


def i_repo(project, name):
    return f'{base_uri}Persistence{project}\\I{filename(name, "Repository")}'


def admin_api_controller(name):
    return f'{base_uri}AdminApi\\Controllers\\{filename(name, "ApiController")}'


def filename(name, postfix):
    return f"{name}{postfix}.cs"

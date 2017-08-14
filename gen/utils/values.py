import gen
from gen.utils import string_utils, file_utils

default_base_uri = "C:\\Users\\Marius\\Source\\Repos\\WaWi_Backend\\"

crud_repository_template = file_utils.get_full_path("templates", "CrudRepositoryTemplate.cs")
icrud_repository_template = file_utils.get_full_path("templates", "ICrudRepositoryTemplate.cs")
searchable_repository_template = file_utils.get_full_path("templates", "SearchableRepositoryTemplate.cs")
isearchable_repository_template = file_utils.get_full_path("templates", "ISearchableRepositoryTemplate.cs")
crud_controller_template = file_utils.get_full_path("templates", "CrudControllerTemplate.cs")
icrud_controller_template = file_utils.get_full_path("templates", "ICrudControllerTemplate.cs")
searchable_controller_template = file_utils.get_full_path("templates", "SearchableControllerTemplate.cs")
isearchable_controller_template = file_utils.get_full_path("templates", "ISearchableControllerTemplate.cs")
crud_api_controller_template = file_utils.get_full_path("templates", "CrudApiControllerTemplate.cs")
searchable_api_controller_template = file_utils.get_full_path("templates", "SearchableApiControllerTemplate.cs")
test_controller_template = file_utils.get_full_path("templates", "ControllerTestTemplate.cs")
test_repository_template = file_utils.get_full_path("templates", "RepositoryTestTemplate.cs")
test_api_controller_template = file_utils.get_full_path("templates", "ApiControllerTestTemplate.cs")


def default_replacers(entity_name, package_name) -> dict:
    return {
        "<#name#>": string_utils.upper_first_letter(entity_name),
        "<#nameLC#>": string_utils.lower_first_letter(entity_name),
        "<#package#>": str.upper(package_name),
        "<#packageLC#>": str.lower(package_name),
        "<#packageFLUC#>": str.capitalize(package_name)
    }

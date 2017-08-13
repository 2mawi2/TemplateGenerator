from gen.utils import string_utils

default_base_uri = "C:\\Users\\Marius\\Source\\Repos\\WaWi_Backend\\"

crud_repository_template = "..\\..\\templates\CrudRepositoryTemplate.cs"
icrud_repository_template = "..\\..\\templates\ICrudRepositoryTemplate.cs"
searchable_repository_template = "..\\..\\templates\SearchableRepositoryTemplate.cs"
isearchable_repository_template = "..\\..\\templates\ISearchableRepositoryTemplate.cs"
crud_controller_template = "..\\..\\templates\CrudControllerTemplate.cs"
icrud_controller_template = "..\\..\\templates\ICrudControllerTemplate.cs"
searchable_controller_template = "..\\..\\templates\SearchableControllerTemplate.cs"
isearchable_controller_template = "..\\..\\templates\ISearchableControllerTemplate.cs"
crud_api_controller_template = "..\\..\\templates\CrudApiControllerTemplate.cs"
searchable_api_controller_template = "..\\..\\templates\SearchableApiControllerTemplate.cs"


def default_replacers(entity_name, package_name):
    return {
        "<#name#>": string_utils.upper_first_letter(entity_name),
        "<#nameLC#>": string_utils.lower_first_letter(entity_name),
        "<#package#>": str.upper(package_name),
        "<#packageLC#>": str.lower(package_name),
        "<#packageFLUC#>": str.capitalize(package_name)
    }

from Utils import StringUtils


def default_replacers(entity_name, package_name):
    return {
        "<#name#>": StringUtils.upper_first_letter(entity_name),
        "<#nameLC#>": StringUtils.lower_first_letter(entity_name),
        "<#package#>": str.upper(package_name),
        "<#packageLC#>": str.lower(package_name),
        "<#packageFLUC#>": str.capitalize(package_name)
    }

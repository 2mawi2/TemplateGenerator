from Generator.Generator import Generator
from Generator.Template import Template

output_uri = "..\content\ExampleRepository.cs"
example_template_uri = "..\content\ExampleTemplate.cs"


def make_templates() -> [Template]:
    """
    Add here the templates you need
    """
    template = Template(example_template_uri, output_uri, "Example")
    return [template]


generator = Generator(make_templates())
generator.generate()

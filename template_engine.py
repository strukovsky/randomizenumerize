from os import path


def render(filename, template_dir="templates", **kwargs):
    template_file = path.join(template_dir, filename)
    with open(template_file, "r") as file:
        contents = file.read()
        for key in kwargs:
            value = str(kwargs[key])
            contents = contents.replace(f'%{key}%', value)
        return contents

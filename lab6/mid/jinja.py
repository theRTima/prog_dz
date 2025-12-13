from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("/"))
template = environment.get_template("message.txt")

print(template.render(the='body_one', go='the variable'))

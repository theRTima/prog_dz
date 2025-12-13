from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("/"))

template = environment.get_template("test_message.txt")

template.render(main_var = "this is a messageß")

from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("/Users/timur/Documents/git/prog_dz/lab6/mid"))

template = environment.get_template("test_message.txt")

print(template.render(main_var = "this is a message"))

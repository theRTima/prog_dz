from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("/Users/timur/Documents/git/prog_dz/lab6/mid"))
template = environment.get_template("template.html")

rendered_html = template.render(body_one="this is a message")

with open("output.html", "w") as page:
    page.write(rendered_html)

print(rendered_html)
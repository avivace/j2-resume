import os
import sys
import json
import jinja2
from jinja2 import Template

latex_jinja_env = jinja2.Environment(
	block_start_string = '\jb{',
	block_end_string = '}',
	variable_start_string = '\jv{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = 'j%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

template = latex_jinja_env.get_template('template-redinter.tex')

with open('data.json', 'r') as file:
	try:
		data = json.loads(file.read())
	except ValueError:
		sys.exit("Not a valid JSON")

with open('resume.tex', 'w') as file:
	file.write(template.render(data=data))
	print("Tex successfully compiled")
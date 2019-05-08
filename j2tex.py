import jinja2
import os
import json
from jinja2 import Template

latex_jinja_env = jinja2.Environment(
	block_start_string = '\jb{',
	block_end_string = '}',
	variable_start_string = '\jv{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = 'J%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

template = latex_jinja_env.get_template('cv.tex')

with open('data.json', 'r') as file:
	data = json.loads(file.read())

with open('cv_render.tex', 'w') as file:
	file.write(template.render(data=data))
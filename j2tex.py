import os
import sys
import json
import jinja2
from jinja2 import Template
import getopt


def main(argv):
    try:
        # -i and -t requires a value,
        opts, args = getopt.getopt(sys.argv[1:], "i:t:o:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    input_file = ""
    template_file = ""

    if "-i" not in [x[0] for x in opts]:
        print("-i <filename> is required")
        usage()
        sys.exit(2)
    if "-t" not in [x[0] for x in opts]:
        print("-t <filename> is required")
        usage()
        sys.exit(2)
    if "-o" not in [x[0] for x in opts]:
        print("-o <filename> is required")
        usage()
        sys.exit(2)
    for option, value in opts:
        if option == "-i":
            input_file = value
        elif option == "-t":
            template_file = value
        elif option == "-o":
            output_file = value

    render(input_file, template_file, output_file)


def usage():
        # TODO
    print("help")


def render(input_file, template_file, output_file):
    latex_jinja_env = jinja2.Environment(
        block_start_string='\jb{',
        block_end_string='}',
        variable_start_string='\jv{',
        variable_end_string='}',
        comment_start_string='\#{',
        comment_end_string='}',
        line_statement_prefix='j%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.abspath('.'))
    )

    template = latex_jinja_env.get_template(template_file)

    with open(input_file, 'r') as file:
        try:
            data = json.loads(file.read())
        except ValueError:
            sys.exit("Not a valid JSON")

    with open(output_file, 'w') as file:
        file.write(template.render(data=data))
        print("Tex successfully compiled")

if __name__ == "__main__":
    main(sys.argv[1:])

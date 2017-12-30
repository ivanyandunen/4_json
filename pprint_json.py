import json
import sys


def load_data(filepath):
    with open(filepath) as jsfile:
        jsfile_content = json.load(jsfile)
    return jsfile_content


def pretty_print_json(jsfile_content):
    print(json.dumps(jsfile_content, sort_keys=True,
                     indent=4, ensure_ascii=False))


if __name__ == '__main__':
    jsfile_content = load_data(sys.argv[1])
    pretty_print_json(jsfile_content)


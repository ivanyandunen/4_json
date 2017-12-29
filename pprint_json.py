import json
import sys


def load_data(filepath):
    with open(filepath) as jsfile:
        data = json.load(jsfile)
    return data


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    pretty_print_json(data)

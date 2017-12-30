import json
import sys


def load_data(filepath):
    with open(filepath) as inputfile:
        inputfile_content = json.load(inputfile)
    return inputfile_content


def pretty_print_json(inputfile_content):
    print(
        json.dumps(
            inputfile_content,
            sort_keys=True,
            indent=4,
            ensure_ascii=False
        )
    )


if __name__ == '__main__':
    try:
        inputfile_content = load_data(sys.argv[1])
        pretty_print_json(inputfile_content)
    except IndexError:
        print("Input file is not specified or missed")

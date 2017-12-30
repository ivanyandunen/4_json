import json
import sys


def load_data(filepath):
    with open(filepath) as input_file:
        input_file_content = json.load(input_file)
    return input_file_content


def pretty_print_json(input_file_content):
    print(
        json.dumps(
            input_file_content,
            sort_keys=True,
            indent=4,
            ensure_ascii=False
        )
    )


if __name__ == '__main__':
    try:
        input_file_content = load_data(sys.argv[1])
        pretty_print_json(input_file_content)
    except (IndexError, FileNotFoundError):
        print("Input file is not specified or missed")
    except json.decoder.JSONDecodeError:
        print("File is incorrect, broken or empty")

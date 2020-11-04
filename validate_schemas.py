from jsonschema import Draft7Validator
from pathlib import Path

import json


def main():
    for filename in Path('target').glob('**/*.schema.json'):
        with open(filename, 'r') as f:
            try:
                Draft7Validator.check_schema(json.loads(f.read()))
                print(str(filename) + ": PASSED")
            except Exception as e:
                print(str(filename) + " failed validation")
                print(e)


if __name__ == "__main__":
    main()

from jsonschema import Draft7Validator
from pathlib import Path

import sys
import json


def main():
    for filename in Path('..').glob('**/*.schema.json'):
        with open(filename,'r') as f:
            try:
                Draft7Validator.check_schema(json.loads(f.read()))
            except:
                print(str(filename) + " failed validation")

            print(str(filename) + ": PASSED")


if __name__ == "__main__":
    main()

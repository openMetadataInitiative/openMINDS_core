from jsonschema import Draft7Validator
from pathlib import Path

import sys
import json


def main():
    for filename in Path('..').glob('**/*.schema.json'):
        with open(filename,'r') as f:
            errors = False
            try:
                Draft7Validator.check_schema(json.loads(f.read()))
                print(str(filename) + ": PASSED")
            except Exception as e:
                print(str(filename) + " failed validation")
                print(e)
                errors = True

    if errors:
        sys.exit(-1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()

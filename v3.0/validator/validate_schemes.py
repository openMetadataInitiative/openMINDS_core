from jsonschema import Draft7Validator
from pathlib import Path

def main():
    for filename in Path('..').glob('**/*.schema.json'):
        print(filename)
        with open(filename,'r') as f:
            print(Draft7Validator.check_schema(f.read()))


if __name__ == "__main__":
    main()

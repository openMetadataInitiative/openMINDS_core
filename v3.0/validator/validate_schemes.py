from jsonschema import Draft6Validator
from pathlib import Path

def main():
    for filename in Path('..').glob('**/*.schema.json'):
        print(filename)
        with open(filename,'r') as f:
            print(f.read())


if __name__ == "__main__":
    main()

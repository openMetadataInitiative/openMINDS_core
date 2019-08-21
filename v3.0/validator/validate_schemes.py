from pathlib import Path

def main():
    for filename in Path('..').glob('**/*.schema.json'):
        print(filename)
        f = open(filename,'r')
        print(f.read())


if __name__ == "__main__":
    main()

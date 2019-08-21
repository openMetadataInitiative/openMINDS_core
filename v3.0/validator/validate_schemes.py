from pathlib import Path

def main():
    for filename in Path('..').glob('**/*.schema.json'):
        print(filename)


if __name__ == "__main__":
    main()

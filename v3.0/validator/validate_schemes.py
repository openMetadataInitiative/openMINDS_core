from pathlib import Path

for filename in Path('..').glob('**/*.schema.json'):
    print(filename)

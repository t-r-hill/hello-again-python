import pathlib

documents = pathlib.Path("/Users/thomashill/Documents/Python")
for file in documents.iterdir():
    print("---------")
    print(file.name)
    print(file.suffix)
    print(file.stem)
    
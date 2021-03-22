import os
from setup import setup

JSONParser = setup()


def main(source="glossary.json"):
    my_parser = JSONParser()

    this_folder = os.path.dirname(__file__)
    source_path = os.path.join(this_folder, source)

    result = my_parser.from_stream(source_path)

    print(f"Input:\n {source} \n")
    print(f"Result\n {result} \n")
    print(f"Result Type\n {type(result)} \n")


if __name__ == "__main__":
    main(source="web_app.json")
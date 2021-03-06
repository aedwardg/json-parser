import os
from jparse.parser import JSONParser


def main(filename="jsons/glossary.json", **kwargs):
    my_parser = JSONParser()

    this_folder = os.path.dirname(__file__)
    json_file = os.path.join(this_folder, filename)

    result = my_parser.from_file(json_file, debug_colors=True, **kwargs)

    print(f"Input:\n {filename} \n")
    print(f"Result\n {result} \n")
    print(f"Result Type\n {type(result)} \n")


if __name__ == "__main__":
    main(filename="jsons/web_app.json", debug=True)

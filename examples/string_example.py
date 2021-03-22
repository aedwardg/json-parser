from setup import setup

JSONParser = setup()

json_string = """
    {"menu": {
      "id": "file",
      "value": "File",
      "popup": {
        "menuitem": [
          {"value": "New", "onclick": "CreateNewDoc()"},
          {"value": "Open", "onclick": "OpenDoc()"},
          {"value": "Close", "onclick": "CloseDoc()"}
        ]
      }
    }}
"""


def main(input_str=json_string):
    my_parser = JSONParser()
    result = my_parser.from_string(input_str)

    print("Input:\n", input_str)
    print("Result\n", result)
    print("Result Type\n", type(result))


if __name__ == "__main__":
    main()

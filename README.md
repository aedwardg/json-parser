# json-parser

A fully-featured LR parser for JSON documents, written in Python using the [parglare](https://github.com/igordejanovic/parglare/) LR/GLR parser framework.

Due to the narrow scope of this project (parsing JSON text), some of parglare's more powerful features (using GLR) are not utilized. However, I tried to make this parser as flexible as possible, allowing users to customize and use many of the LR features available.

## Usage

The [`JSONParser`](https://github.com/aedwardg/json-parser/blob/main/jparse/parser.py) class provides three methods that handle the parsing of JSON text:

- `from_file()`
- `from_string()` and
- `from_stream()`

As the names suggest, these methods allow you to supply your JSON text in 3 ways: as a string, as a file (calling parglare's `Parser.parse_file()`), or as a stream &mdash; i.e. by supplying a source to be used with Python's `with open() as` syntax.

### Grammar and Parser arguments

Due to the structure of the `JSONParser` class, only keyword arguments that exist in both the Parser and Grammar classes can be directly passed to the three `JSONParser` methods, such as `debug` and `debug_colors`.

#### Actions

By default, all three methods are called with `cleaned=True`, which applies [specific grammar actions](https://github.com/aedwardg/json-parser/blob/main/jparse/json_actions.py) to deserialize the JSON input to a native Python object, similar to Python's built-in `json.load` and `json.loads`. Specifying `cleaned=False` in any of the methods will turn off these actions and return the pure parse result with no additional semantic actions applied. If instead you would like to use your own custom actions, you can do so by supplying your actions dictionary at instantiation:

```python
my_parser = JSONParser(actions=my_action_dict)
```

If you have supplied your own actions, the `cleaned` keyword argument will now apply to your actions, where `True` enables them and `False` disables them.  
_For more information on actions, see the [parglare documentation](http://www.igordejanovic.net/parglare/stable/actions/)._

#### Building the Parse Tree

If you need to build and view the entire [parse tree](http://www.igordejanovic.net/parglare/stable/parse_trees/), the `build_tree` option is available during instantiation, rather than within the methods themselves:

```python
my_parser = JSONParser(build_tree=True)
```

When `build_tree` is set to `True`, the parser will print the entire parse tree to the terminal. If using the included examples, you will see the following printed to the terminal in this order:

1. The parse tree
2. The input (either full string or file name)
3. The resulting Parser object (not the deserialized JSON), e.g., `<NonTerm(start=5, end=286, sym=JSON)>`
4. The Python type of the parser object, e.g., `<class 'parglare.parser.NodeNonTerm'>`

This is because parglare's Parser returns the final node rather than the parse result when the `build_tree` option is selected.

_NOTE: For now the parse tree is printed to the terminal, but in the future I would like to have it write to a separate file since Windows terminals have a maximum scrollback of 10,000 lines and parse trees are usually longer than that._

## Try It Out

To try the JSONParser locally, use the following steps:

1. Ensure you have Python 3.6 or above installed. You can download it [here](https://www.python.org/downloads/) if you don't already have it.
2. Clone the repository to your computer (instructions [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)).
3. Navigate to the json-parser directory and create and activate a virtual environment with these commands:

   ```bash
   $ cd json-parser/
   $ python -m venv venv
   $ source venv/bin/activate
   ```

   For Windows users using CMD, replace the activation command with

   ```cmd
   venv\Scripts\activate
   ```

   or for those using a bash terminal on Windows, replace the activation command with

   ```bash
   $ source venv/Scripts/activate
   ```

4. With your virtual environment activated, install this package locally:

   ```bash
   $ python -m pip install -e .
   ```

   _Note: Don't forget the period at the end! This command will also install parglare in your virtual environment._

5. Run the examples!

   - You can run the examples as-is, like you would any Python file:

     ```bash
     $ cd examples
     $ python ./string_example.py
     ```

   - You can also define your own strings for `string_example.py`, change the JSON files parsed in `file_example.py` and `stream_example.py` or change any of the options as discussed above in the [Usage](#usage) section.
     - Note that if you want to parse a JSON file not included in the `examples/jsons` directory, the easiest way is to move it into that directory and follow the naming convention that's in the examples. Both `from_file()` and `from_stream()` take absolute paths, but the file and stream examples have been modified to use paths relative to their directory (`json-parser/examples`).

## Attribution

The [JSONParser grammar](https://github.com/aedwardg/json-parser/blob/main/jparse/jsongrammar.pg) is loosely based on the McKeeman Grammar described at [json.org](https://www.json.org), with some additional changes to accommodate parglare's pure BNF grammar with syntactic sugar. Additionally, parglare automatically ignores whitespace, so additional whitespace grammar rules were not needed.

All example JSON files are also from [json.org](https://json.org/example.html) for ease of use and consistency.

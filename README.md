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

This is because parglare's Parser returns the final node rather than the parse result when the `build_tree` object is selected.

_NOTE: For now the parse tree is printed to the terminal, but in the future I would like to have it write to a separate file since Windows terminals have a maximum scrollback of 10,000 lines and parse trees are usually longer than that._

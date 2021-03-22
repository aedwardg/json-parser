import os
from parglare import Grammar, Parser
from .json_actions import action


class JSONParser:
    grammar = os.path.join(os.path.dirname(__file__), "jsongrammar.pg")

    def __init__(self, actions=action.all, build_tree=False):
        self.actions = actions
        self.build_tree = build_tree

    def fetch_tree(self, result):
        if self.build_tree:
            print(result.tree_str())
        else:
            info_message = """
                JSONParser initialized with `build_tree=False`.
                To view the parse tree, initialize with `build_tree=True`.
            """
            print(info_message)

    def from_file(self, filename, cleaned=True, **kwargs):
        actions = self.actions if cleaned else None
        g = Grammar.from_file(self.grammar, **kwargs)
        parser = Parser(g, actions=actions, build_tree=self.build_tree, **kwargs)

        result = parser.parse_file(file_name=filename)
        self.fetch_tree(result)

        return result

    def from_string(self, input_str, cleaned=True, **kwargs):
        actions = self.actions if cleaned else None
        g = Grammar.from_file(self.grammar, **kwargs)
        parser = Parser(g, actions=actions, build_tree=self.build_tree, **kwargs)

        result = parser.parse(input_str)
        self.fetch_tree(result)

        return result

    def from_stream(self, source, cleaned=True, **kwargs):
        actions = self.actions if cleaned else None
        g = Grammar.from_file(self.grammar, **kwargs)
        parser = Parser(g, actions=actions, build_tree=self.build_tree, **kwargs)

        with open(source, "r") as f:
            result = parser.parse(f.read())

        self.fetch_tree(result)

        return result

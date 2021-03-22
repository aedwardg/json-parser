import os
from parglare import Grammar, Parser
from .json_actions import action


class JSONParser:
    grammar = os.path.join(os.path.dirname(__file__), "jsongrammar.pg")

    def __init__(self, actions=action.all):
        self.actions = actions

    def from_file(self, filename, cleaned=True, **kwargs):
        actions = self.actions if cleaned else None
        g = Grammar.from_file(self.grammar, **kwargs)
        parser = Parser(g, actions=actions, **kwargs)

        result = parser.parse_file(file_name=filename)
        return result

    def from_string(self, input_str, cleaned=True, **kwargs):
        actions = self.actions if cleaned else None
        g = Grammar.from_file(self.grammar, **kwargs)
        parser = Parser(g, actions=actions, **kwargs)

        result = parser.parse(input_str)
        return result

    def from_stream(self, source, cleaned=True, **kwargs):
        actions = self.actions if cleaned else None
        g = Grammar.from_file(self.grammar, **kwargs)
        parser = Parser(g, actions=actions, **kwargs)

        with open(source, "r") as f:
            result = parser.parse(f.read())
        return result

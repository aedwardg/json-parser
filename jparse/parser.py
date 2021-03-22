import os
from parglare import Grammar, Parser
from .json_actions import action


class JSONParser:
    grammar = os.path.join(os.path.dirname(__file__), "jsongrammar.pg")

    def __init__(self):
        self.actions = action.all

    def from_file(self, filename):
        g = Grammar.from_file(self.grammar)
        parser = Parser(g, actions=self.actions)

        result = parser.parse_file(file_name=filename)
        return result

    def from_string(self, input_str):
        g = Grammar.from_file(self.grammar)
        parser = Parser(g, actions=self.actions)

        result = parser.parse(input_str)
        return result

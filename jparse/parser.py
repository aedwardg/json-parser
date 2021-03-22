import os
from parglare import Grammar, Parser


class JSONParser:
    grammar = os.path.join(os.path.dirname(__file__), "jsongrammar.pg")

    def __init__(self):
        self.actions = {
            "Object": self.object_action,
        }

    def object_action(self, context, nodes):
        # Objects look like this before action:
        # ['{', [['key', ':', 'value'], ['key', ':', 'value'], ...], '}']
        if len(nodes) > 2:
            members = nodes[1:-1][0]
            return {member[0]: member[2] for member in members}
        else:
            return {}

    def from_file(self):
        pass

    def from_string(self, input_str):
        g = Grammar.from_file(self.grammar)
        parser = Parser(g, actions=self.actions)

        result = parser.parse(input_str)
        return result

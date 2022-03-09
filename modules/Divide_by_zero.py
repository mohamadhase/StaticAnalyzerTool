from pprint import pprint


class Divide_by_zero:

    def __init__(self, lines, tokens) -> None:

        self.lines = lines
        self.tokens = tokens

    def handle_zero(self):

        pprint(self.tokens)
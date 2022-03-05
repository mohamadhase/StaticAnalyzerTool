from pprint import pprint


class Three_parameters:

    def __init__(self, tokens: list) -> None:

        self.tokens = tokens
        self.functions = []

        for key, value in tokens.items():
            if value['Type'] == 'Function':
                self.functions.append(key)

    def handle_parameters(self) -> None:
        """function that chaek number of parameters in each function
        and print message to change parameters
        """

        for func in self.functions:
            if ',' in func and func.count(',') > 2:
                print('more than three parameters in this function =>', func)
from pprint import pprint


class Parameters:

    def __init__(self, tokens: list) -> None:
        """init function to initialize main attributes for use in anther functions

        Args:
            tokens (list): token from file code.txt containing lines and type of line
        """

        self.tokens = tokens
        self.functions = []

        for key, value in tokens.items():
            if value['Type'] == 'Function':
                self.functions.append(key)

    def handle_three_parameters(self) -> list:
        """function that chaek number of parameters in each function
        and print message to change parameters
        """
        rsualt = []
        for function in self.functions:
            if ',' in function and function.count(',') > 2:
                rsualt.append(function)

        return rsualt
from Const import Const
from Data import Data
from Three_parameters import Three_parameters
from MagicNumbers import MagicNumbers


def main():
    data = Data("code.txt")
    data.tokinizer()
    print(Const.variables_value)

    three_parameters = Three_parameters(data.tokens)
    print('handle_parameters :')
    three_parameters.handle_parameters()

    magic_numbers = MagicNumbers(data.tokens)
    print('handle_magic_numbers :')
    magic_numbers.handle_magic_numbers_in_if_statments()


if __name__ == "__main__":
    main()

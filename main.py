from Const import Const
from Data import Data
from Three_parameters import Three_parameters


def main():
    data = Data("code.txt")
    data.tokinizer()
    print(Const.variables_value)

    three_parameters = Three_parameters(data.tokens)
    print('handle_parameters :')
    three_parameters.handle_parameters()


if __name__ == "__main__":
    main()

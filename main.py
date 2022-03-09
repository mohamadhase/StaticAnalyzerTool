from modules.Const import Const
from modules.Data import Data
from modules.Parameters import Parameters
from pprint import pprint


def main():

    data = Data("code.txt")
    data.tokinizer()
    parameters = Parameters(data.tokens)

    parameters.handle_attribute()

    # handle more then three parameters


if __name__ == "__main__":
    main()

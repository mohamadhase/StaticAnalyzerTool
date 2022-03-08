from modules.Const import Const
from modules.Data import Data
from modules.Parameters import Parameters
from pprint import pprint


def main():

    data = Data("code.txt")
    data.tokinizer()
    parameters = Parameters(data.tokens)

    #pprint(Const.variables_value)

    # handle more then three parameters
    print('handle_parameters :-')
    for function in parameters.handle_three_parameters():
        print('more than three parameters in this function =>', function)


if __name__ == "__main__":
    main()

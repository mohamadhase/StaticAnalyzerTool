from modules.Const import Const
from modules.Data import Data
from modules.Parameters import Parameters
from modules.MagicNumbers import MagicNumbers
from modules.UnReachableCode import UnReachableCode
from pprint import pprint


def main():

    data = Data("code.txt")
    data.tokinizer()
    parameters = Parameters(data.tokens)

    parameters.handle_attribute()

    # handle more then three parameters

    magic_numbers = MagicNumbers(data.tokens)
    print('handle_magic_numbers :')
    magic_numbers.handle_magic_numbers(data.tokens)
        
if __name__ == "__main__":
    main()

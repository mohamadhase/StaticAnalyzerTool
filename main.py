from modules.Const import Const
from modules.Data import Data
from modules.Parameters import Parameters
from modules.MagicNumbers import MagicNumbers
from modules.UnReachableCode import UnReachableCode
from modules.Print import Print
from pprint import pprint


def main():

    data = Data("code.txt")
    data.tokinizer()

    parameters = Parameters(data.tokens)
    #solve the number of attributes
    parameters.handle_three_parameters()
    #solve the number of type and size match  when call function
    parameters.handle_attribute()

    magic_numbers = MagicNumbers(data.tokens)
    magic_numbers.handle_magic_numbers()

    unreachable_code = UnReachableCode(data)
    unreachable_code.body_of_functions()
    unreachable_code.handle_alone_return()
    unreachable_code.handle_if_return()
    unreachable_code.handle_same_logic()

    print = Print(data, magic_numbers, unreachable_code, parameters)
    print.print_results()


if __name__ == "__main__":
    main()

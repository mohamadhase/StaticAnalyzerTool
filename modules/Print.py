from modules.Const import Const
from modules.Data import Data
from modules.Parameters import Parameters
from modules.MagicNumbers import MagicNumbers
from modules.UnReachableCode import UnReachableCode
from pprint import pprint


class Print:

    def __init__(self, data: Data, magic_number: MagicNumbers,
                 unreachable_code: UnReachableCode, parameters: Parameters):
        self.data = data
        self.magic_number = magic_number
        self.unreachable_code = unreachable_code
        self.parameters = parameters

    def print_results(self):

        self.__print_magic()

        self.__print_unreachable()

        self.__print_paramerters()

    def __print(self, header_message: str, err_message: str,
                list_errors: list):
        #Console Print
        printed_lines = []
        message = ""
        pprint("=" * 10 + f" {header_message} : " + "=" * 10)
        for line in list_errors:
            line_number = self.data.lines.index(line) + 1

            message = f" {err_message} : {line_number} "
            printed_lines.append(message + "\n")
            pprint(message)

            message = f"    {line} "
            printed_lines.append(message + "\n")
            pprint(message)

            message = "_" * 45
            printed_lines.append(message + "\n")
            pprint(message)

            message = "+" * 60
            printed_lines.append(message + "\n")
            pprint(message)

        #File Print
        #Clear file before Run becouse python is crazy  :) w+ mode is not working in my device
        with open("result.txt", "a") as text_file:
            for line in printed_lines:
                text_file.write(line)

    def __print_magic(self):
        self.__print("Magic Number Results",
                     "Magic Number detected in line number",
                     self.magic_number.result)

    def __print_unreachable(self):
        temp_result = [
            line for line in self.unreachable_code.result
            if not line.__contains__("{") and not line.__contains__("}")
            and not line == ""
        ]
        self.__print("Unreachable Code Results",
                     "Unreachable Code detected in line number", temp_result)

    def __print_paramerters(self):
        self.__print("Number of parameters Results",
                     "more than three parameters detected in line number",
                     self.parameters.result_three_parameters)

        self.__print("Type and size match Results",
                     "type and size issue detected in line number",
                     self.parameters.result_handle_attribute)

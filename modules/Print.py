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

    def __print_magic(self):
        pprint("=" * 10 + " Magic Number Results : " + "=" * 10)
        for line in self.magic_number.result:
            line_number = self.data.lines.index(line) + 1
            pprint(f" Magic Number detected in line number :  {line_number} ")
            pprint(f"    {line} ")
            pprint("_" * 45)
        pprint("+" * 60)

    def __print_unreachable(self):
        pprint("=" * 10 + " Unreachable Code Results : " + "=" * 10)
        for line in self.unreachable_code.result:
            if not line.__contains__(
                    "{") and line != "" and not line.__contains__("}"):
                line_number = self.data.lines.index(line) + 1
                pprint(
                    f" Unreachable Code detected in line number :  {line_number} "
                )
                pprint(f"    {line} ")
                pprint("_" * 45)
        pprint("+" * 60)

    def __print_paramerters(self):
        pprint("=" * 10 + "Nubmer of parameters Results : " + "=" * 10)
        for line in self.parameters.result_three_parameters:
            line_number = self.data.lines.index(line) + 1
            pprint(
                f" more than three parameters detected in line number :  {line_number} "
            )
            pprint(f"    {line} ")
            pprint("_" * 45)
        pprint("+" * 60)

        pprint("=" * 10 + " Type and size match Results : " + "=" * 10)
        for line in self.parameters.result_handle_attribute:
            line_number = self.data.lines.index(line) + 1
            pprint(
                f" type and size issue detected in line number :  {line_number} "
            )
            pprint(f"    {line} ")
            pprint("_" * 45)
        pprint("+" * 60)

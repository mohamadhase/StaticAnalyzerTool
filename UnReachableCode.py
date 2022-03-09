from tkinter.messagebox import NO
from Const import Const
from Data import Data


class UnReachableCode:

    def __init__(self, data: Data) -> None:
        """    
        This class read the code and extract any line marked as unreachable
        Args:
            data (Data): 
            this Object of Type class Data contain the source code as a text
        """

        #this attribute contains the body of each function in the source code
        self.code_block = []
        self.lines = data.lines
        self.tokens = data.tokens
        #this attribute contains each line marked as unreachable code
        self.result = []

    def codeCutter(self):
        """
        this function responsible for get the body of each function and store it in self.code_block
        """
        functin_body = ""
        Function_detected = False
        if_counter = 0

        for line in self.lines:

            if Function_detected == True:
                functin_body += line + "\n"

            if self.tokens[line]["Type"] == "Function":
                Function_detected = True

            if line.__contains__("if") or line.__contains__(
                    "else") or line.__contains__("else if"):
                if_counter += 1

            if (line.__contains__("}")):

                if if_counter == 0:
                    Function_detected = False
                    self.code_block.append(functin_body)
                    functin_body = ""

                else:
                    if_counter -= 1

    def codeTrace(self)->None:
        """
        this function should read the code line by line and detect any line
        will be unreachable and store the result in self.result
        """

        ## return alone handle
        for block in self.code_block:
            return_detected = False
            Number_of_blocks = 0

            for line in block.split("\n"):

                if return_detected == True:
                    if line not in self.result:
                        self.result.append(line)

                if line.__contains__("return ") and Number_of_blocks == 0:              
                    return_detected = True

                if line.__contains__("if") or line.__contains__("else"):
                    Number_of_blocks += 1

                if line.__contains__("}"):
                    Number_of_blocks -= 1


        #handle if
        for block in self.code_block:

            if_else_return = []
            if_flag = True
            started = False
            done_here = False
            last = False
            status = ""
            if_count = 0

            for line in block.split("\n"):

                if status == "none_reachable":
                    
                    if line not in self.result:
                        self.result.append(line)

                if line.__contains__("if") and if_flag == True:
                    if_flag = False
                    started = True
                    if_count += 1

                elif line.__contains__("if "):
                    if_count += 1

                if started == True:

                    if last == True and line.__contains__(
                            "}") and if_count == 0:
                            
                        if all(if_else_return):
                            status = "none_reachable"

                        else:
                            status = "reachable"

                    if line.__contains__("return ") and done_here == False:
                        done_here = True
                        if_else_return.append(True)

                    if line.__contains__("}"):
                        done_here = False

                        if if_count > 0:
                            if_count -= 1

                    if line.__contains__("else ") and not line.__contains__(
                            "else if") and if_count == 0:
                        last = True

            #handle same if

            for block in self.code_block:

                all_if_conditions = []
                ifs_returned = []
                in_if = False
                status = ""

                for line in block.split("\n"):

                    if status == "Non reachable":

                        if line not in self.result:
                            self.result.append(line)

                        if line.__contains__("}"):
                            status = ""

                    if (line.__contains__("if ")):
                        in_if = True
                        condition = line.split(" ")[-1]

                        if condition in all_if_conditions:
                            index = all_if_conditions.index(condition)

                            if (ifs_returned[index] == True):
                                status = "Non reachable"

                        else:
                            all_if_conditions.append(condition)
                            
                    if (line.__contains__("return ") and in_if == True):
                        ifs_returned.append(True)

                    if (line.__contains__("}")):
                        in_if = False

from Const import Const

class Data:
    """
    class for read the data from the txt file and get it ready to be used in other classes
    """

    def __init__(self, file_name):
        """
        1) read the data from text file 
        2) split the data into lines and store it in lines variable
        3) initialize tokens dictinary to store tha type of each line in it
        Args:
            file_name (String): the name of text file contains the c++ source code to be checked
        """
        self.data = open(file_name).read()
        self.lines = self.data.split("\n")
        self.tokens = {}

    def tokinizer(self) ->None:
        """
        this function give each line in the source code token to recognize it 
        """
        for line in self.lines:
            if line.startswith("//"):
                self.tokens[line] = {"Type": "Comment"}

            elif line.startswith("class"):
                self.tokens[line] = {"Type": "Class"}

            elif any(map(line.startswith,
                         Const._data_type)) and line.endswith(")"):
                self.tokens[line] = {"Type": "Function"}
                self.functionParameters(line)

            elif line.startswith("cout <<") or line.startswith("cout<<"):
                self.tokens[line] = {"Type": "Print"}


            elif line.startswith("if") and line.endswith(")"):
                self.tokens[line] = {"Type": "If"}
            
            elif line.__contains__("return "):
                self.tokens[line] = {"Type": "exit"}

            elif any(map(line.startswith,
                         Const._data_type)) and (line.__contains__("=")
                                                 or line.__contains__(";")):
                self.tokens[line] = {"Type": "Declaration"}
                self.declarationToken(line)
            
            elif line.startswith("cin") and line.__contains__(">>"):
                self.tokens[line] = {"Type": "Input"}
            elif any(map(line.__contains__, Const._operations)) and not any(
                    map(line.startswith, Const._data_type)):
                self.tokens[line] = {"Type": "Operation"}

            else:
                self.tokens[line] = {"Type": "None"}

    def declarationToken(self, line: str) -> None:
        """
        this function takes the lines tokonized as a declaration line and add the variable with its value 
        to variables_value dict

        Args:
            line (str): line contains variable to be declare 
        """
        value = 0
        if line.__contains__("="):
            value = line.split(" ")[-2]

        if (any(map(line.__contains__, Const._operations))):
            value = eval(value, Const.variables_value)

        Const.variables_value[line.split(" ")[1]] = int(value)
        Const.Variables_status[line.split(" ")[1]] = {"changed":False,"checked":False}
    def functionParameters(self,line:str)->None:
        """
        this function get the variables from the the parameters and store them in the Variables_value dict

        Args:
            line (str): line tokenized as declaration for a function
        """
        first_index = line.index("(")
        last_index = line.index(")")
        parameters = line[first_index+1:last_index]
        if(parameters.count(",")==0):
            return
        parameters = parameters.split(",")
        for parameter in parameters:
            parameter_name = parameter.split(" ")[-1]
            Const.variables_value[parameter_name] = 0
            Const.Variables_status[parameter_name] = {"changed":False,"checked":False,"input":False}


            


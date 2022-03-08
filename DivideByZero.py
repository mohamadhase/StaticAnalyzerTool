from re import T
from tkinter import Variable
from Data import Data
from Const import Const
class DivideByZero:
    def __init__(self,data:Data):

        self.blocks =[]

        pass

    def blockMaker(self,data:Data):

        line_ = ""
        flag = False
        for line in data.lines:
            if flag==True:
                line_+=line+"\n"

            if data.tokens[line]["Type"]=="Function":
                flag = True
                line_+=line+"\n"
                continue
            elif line.__contains__("}") and line_!="":
                flag=False
                self.blocks.append(line_)
                line_=""



    
    def traceCode(self,data:Data):
        for block in self.blocks:
            variables_status = Const.Variables_status
            variables_value = Const.variables_value
            checked_variables = []
            divide = False
            for block_line in block.split("\n"):
                if data.tokens[block_line]["Type"]=="Operation":
                    if not block_line.__contains__("/"):
                        value = 0
                        if block_line.__contains__("="):
                            value = block_line.split(" ")[-2]

                        if (any(map(block_line.__contains__, Const._operations))):
                            value = eval(value, Const.variables_value)
                        variables_value[block_line.split(" ")[1]] = int(value)
                        variables_status[block_line.split(" ")[1]]["changed"]=True
                    else:

                        if (block_line.split(" ")[1] in checked_variables and divide ==True) or  :
                            print(f"{block_line}-> has no issue")
                        else: 
                            print(f"{block_line}->   issue")

                if data.tokens[block_line]["Type"]=="Input":
                    variables_status[block_line.split("")[-2]]["input"]=True

                if data.tokens[block_line]["Type"]=="If":
                    condition:str = block_line.split(" ")[-1]
                    if(condition.__contains__("<0")):#divide
                        start_index = condition.index("(")
                        end_index = condition.index("<")
                        variable_name = condition[start_index+1:end_index]
                        checked_variables.append(variable_name)
                        divide = True
                        pass

                    elif(condition.__contains__(">=0")):#return
                        pass

                    elif(condition.__contains__("==0")):#return
                        pass

                    elif( not any(map(condition.__contains__,Const._logical_operations))):#divide
                        pass

                    elif(condition.__contains__(">0")):#divide
                        pass

                    elif(condition.__contains__("!=0")):#divide
                        pass

                    elif(condition.__contains__("<=0")):#return
                        pass


                
                    
    

        
                
        


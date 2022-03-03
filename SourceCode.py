


from ast import Pass
from lib2to3.pgen2.token import OP
from tkinter import Variable
from unittest import case


class Const : 
    DATATYPE=["int","float","double","long","char"]
    OPERATIONS = ["+","-","*","/","++","--","*=","-=","/=","+="]
    VARIABLES = {}
class Data:
    def __init__(self,file_name):
        self.data = open(file_name).read()
        self.lines = self.data.split("\n")
        self.tokens = {}
    def tokinizer(self):
        for i in self.lines:
            if i.startswith("//"):
                self.tokens[i]= {"Type":"Comment"}
            elif i.startswith("class"):
                self.tokens[i]= {"Type":"Class"}
            elif any(map(i.startswith,Const.DATATYPE)) and i.endswith(")"):
                self.tokens[i]={"Type":"Function"}
            elif i.startswith("cout<<"):
                self.tokens[i]={"Type":"Print"}
            elif any(map(i.startswith,Const.DATATYPE)) and (i.__contains__("=") or i.__contains__(";")):
                self.tokens[i] = {"Type":"Declaration"}
                self.declarationToken(i)
            elif any(map(i.__contains__,Const.OPERATIONS)) and not any(map(i.startswith,Const.DATATYPE)):
                self.tokens[i] = {"Type":"Operation"}
            else :
                self.tokens[i] = {"Type":"None"}

    def declarationToken(self,i:str):
        print("--------------------")
        value = 0

        if i.__contains__("="):
            value = i.split(" ")[-2]
        if (any(map(i.__contains__,Const.OPERATIONS))):
            if(i.split(" ")[-2].__contains__("-")):
                value1 = int(Const.VARIABLES[i.split(" ")[-2].split("-")[0]]["Value"])
                value2 = int(Const.VARIABLES[i.split(" ")[-2].split("-")[1]]["Value"])
                value = value1-value2

        if i.split(" ")[1] in Const.VARIABLES.keys():
            Const.VARIABLES[i.split(" ")[1]]["Value"]=value
            Const.VARIABLES[i.split(" ")[1]]["Changed"]=False
        else:
            Const.VARIABLES[i.split(" ")[1]]={
                "Value":value,
                "Changed":False
            }



class DivideByZero:
    def moveForword(data:Data):
        temp_tokens = data.tokens
        for i in data.lines:
            if temp_tokens[i]["Type"]=="Function":
                temp_tokens = data.tokens
            if temp_tokens[i]["Type"]=="Operation":
                if any(map(temp_tokens[i]["Value"].__contains__,Const.OPERATIONS)):
                    pass
                    


                

            
     

            





        

                  

        
    
def main():
    data = Data("code.txt")
    data.tokinizer()
    print(Const.VARIABLES)
    DivideByZero.moveForword(data)
    pass
    
if __name__ =="__main__":
    main()





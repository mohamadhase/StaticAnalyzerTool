


from tkinter import Variable


class Const : 
    DATATYPE=["int","float","double","long"]
    OPERATIONS = ["+","-","*","/","++","--","*=","-=","/=","+="]
    VARIABLES = []
class Data:
    def __init__(this,file_name):
        this.data = open(file_name).read()
        this.lines = this.data.split("\n")
        this.tokens = {

        }
    def tokinizer(this):
        for i in this.lines:
            if i.startswith("//"):
                this.tokens[i]= {"Type":"Comment"}
            elif i.startswith("class"):
                this.tokens[i]= {"Type":"Class"}
            elif any(map(i.startswith,Const.DATATYPE)) and i.endswith(")"):
                this.tokens[i]={"Type":"Function"}
            elif i.startswith("cout<<"):
                this.tokens[i]={"Type":"Print"}
            elif any(map(i.startswith,Const.DATATYPE)) and (i.__contains__("=") or i.__contains__(";")):
                this.tokens[i] = {"Type":"Declaration"}
                Const.VARIABLES.append(i.split(" ")[1])
            elif any(map(i.__contains__,Const.OPERATIONS)) and not any(map(i.startswith,Const.DATATYPE)):
                this.tokens[i] = {"Type":"Operation"}

            





        

                  

        
    
def main():
    data = Data("code.txt")
    data.tokinizer()

    pass
    
if __name__ =="__main__":
    main()





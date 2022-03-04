from Const import Const
from Data import Data
  
def main():
    data = Data("code.txt")
    data.tokinizer()
    print(Const.variables_value)
    pass
    
if __name__ =="__main__":
    main()





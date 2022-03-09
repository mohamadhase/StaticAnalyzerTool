from modules.Const import Const

class MagicNumbers:
    result = []
    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
    
    def contain_digit(self,line) -> bool:
        """
        function that check the line if contain number or not.
        """
        containMagic = False
        for cell in line:
            if cell.isdigit():
                containMagic = True
        return containMagic
        
    def handle_magic_numbers(self) -> None:
        """
        function that check each line in file if contain any type of magic 
        number, in the end it will return all lines that contain magic number in list.
        """
        containMagic = False
        for line in self.tokens:
            if line.__contains__('cout'):
                if any(map(line.__contains__, Const._operations)):
                    containMagic = self.contain_digit(line)
                
            elif not line.__contains__('cout') and not any(map(line.startswith, Const._data_type)) :
                containMagic = self.contain_digit(line)
                if '"' in line and (line.count('"') % 2 == 0) and line.count('"') != 0:
                 containMagic = True
                
            elif any(map(line.startswith, Const._data_type)) and any(map(line.__contains__, Const._operations)):
                containMagic = self.contain_digit(line)
                
            
            if containMagic == True:
                self.result.append(line)
                containMagic == False

from functools import cache
from Const import Const


class Data:
    '''
    class for read the data from the txt file and get it ready to be used in other classes
    '''

    def __init__(self, file_name):
        '''
        1) read the data from text file 
        2) split the data into lines and store it in lines variable
        3) initialize tokens dictinary to store tha type of each line in it
        Args:
            file_name (String): the name of text file contains the c++ source code to be checked
        '''
        self.data = open(file_name).read()
        self.lines = self.data.split('\n')
        self.tokens = {}

    def tokinizer(self) -> None:
        '''
        this function give each line in the source code token to recognize it 
        '''
        for line in self.lines:
            if line.startswith('//'):
                self.tokens[line] = {'Type': 'Comment'}

            elif line.startswith('class'):
                self.tokens[line] = {'Type': 'Class'}

            elif any(map(line.startswith,
                         Const._data_type)) and line.endswith(')'):
                self.tokens[line] = {'Type': 'Function'}

            elif line.startswith('cout <<') or line.startswith('cout<<'):
                self.tokens[line] = {'Type': 'Print'}

            elif any(map(line.startswith,
                         Const._data_type)) and (line.__contains__('=')
                                                 or line.__contains__(';')):
                self.tokens[line] = {'Type': 'Declaration'}
                self.declarationToken(line)

            elif any(map(line.__contains__, Const._operations)) and not any(
                    map(line.startswith, Const._data_type)):
                self.tokens[line] = {'Type': 'Operation'}

            else:
                self.tokens[line] = {'Type': 'None'}

    def declarationToken(self, line: str) -> None:
        '''
        this function takes the lines tokonized as a declaration line and add the variable with its value 
        to variables_value dict

        Args:
            line (str): line contains variable to be declare 
        '''
        value = 0
        if line.__contains__('='):
            value = line.split(' ')[-2]

        try:
            if (any(map(line.__contains__, Const._operations))):

                value = eval(
                    line.split(' ')[-1].replace(';', ''),
                    Const.variables_value)

        except Exception as e:
            print("Exception" + str(e))
            exit()

        try:
            Const.variables_value[line.split(' ')[1]] = int(value)

        except Exception as e:
            print("Exception" + str(e))
            exit()

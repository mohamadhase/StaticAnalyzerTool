
class MagicNumbers:

    def __init__(self, tokens: list) -> None:
        self.tokens = tokens
        self.Ifs = self.initialize_lines(tokens,'If')
        self.returns = self.initialize_lines(tokens,'Return')
        self.fors = self.initialize_lines(tokens,'For')
        self.whiles = self.initialize_lines(tokens,'While')
        self.calling_finction = self.initialize_lines(tokens,'calling_finction')


    def implementation(self) -> None:
        self.handle_magic_numbers(self.Ifs)
        self.handle_magic_numbers(self.returns)
        self.handle_magic_numbers(self.whiles)
        self.handle_magic_numbers(self.fors)
        self.handle_magic_numbers(self.calling_finction)

    def initialize_lines(tokens,type) -> list:
        temp = []
        for key, value in tokens.items():
            if value['Type'] == type:
                temp.append(key)
        return temp


    def handle_magic_numbers(magic_type) -> None:
        containMagic = False
        for line in magic_type:
            for digit in line:
                if digit.isdigit():
                    containMagic = True

            if '"' in line and (line.count('"') % 2 == 0) and line.count('"') != 0:
                containMagic = True
            
        if containMagic == True:
            print("this line contain magic number => ",line)





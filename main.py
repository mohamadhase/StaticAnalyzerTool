from Const import Const
from Data import Data
from Three_parameters import Three_parameters
from UnReachableCode import UnReachableCode


def main():
    data = Data("code.txt")
    data.tokinizer()

    # three_parameters = Three_parameters(data.tokens)
    # print('handle_parameters :')
    # three_parameters.handle_parameters()
    unreachablecode = UnReachableCode(data)
    unreachablecode.codeCutter()
    unreachablecode.codeTrace()
if __name__ == "__main__":
    main()

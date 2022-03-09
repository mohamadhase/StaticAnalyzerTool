import re


class Parameters:

    def __init__(self, tokens: list) -> None:
        """init function to initialize main attributes for use in anther functions

        Args:
            tokens (list): token from file code.txt containing lines and type of line
        """
        self.tokens = tokens
        self.functions = []  # store every functions
        self.call_function = []  # every call function in the code
        self.function_calls = {}  # every function with his calls
        self.name_prototype = {}  # every nmae of function with prototype
        self.result_handle_attribute = []
        self.result_three_parameters = []

        for key, value in tokens.items():
            if value['Type'] == 'Function' and 'main' not in key:  # we don't care about the main function
                self.functions.append(key)

            elif value['Type'] == 'CallFunction':
                self.call_function.append(key)

    def handle_three_parameters(self) -> list:
        """function that chaek number of parameters in each function
        and return list of functions that have more than three parameters
        """
        for function in self.functions:
            if ',' in function and function.count(',') > 2:
                self.result_three_parameters.append(function)

    def handle_attribute(self) -> list:
        """function that chaek order of data types in each function,
        and check value passed in the call each function

        Returns:
            list[tupel]: list contains functions and calls within incorrect 
        """

        self.__function_and_calls()

        for key in self.function_calls.keys():
            args = key[key.index('(') + 1:key.index(')')].split(
                ',')  # to take argumant without name and data type of function

            calls = self.function_calls[key]  #  to take evrey call function

            data_type_args = self.__data_type_function(args)
            len_data_type = len(data_type_args)

            if not self.__check_data_type_order(
                    data_type_args
            ):  # check if function with correct order of data type
                self.result_handle_attribute.append(
                    ('order data type in function is not correct', key))
                continue

            for call in calls:
                valus_in_call = call[call.index('(') +
                                     1:call.index(')')].split(
                                         ',')  # take vaules in call function

                if len_data_type == 1:
                    if not (valus_in_call[0].replace(
                            ' ', '').isdecimal()):  # check is intager number
                        self.result_handle_attribute.append(
                            ('1 this call is not correct ', call))

                elif len_data_type == 2:
                    if not (valus_in_call[0].replace(
                            ' ', '').isdecimal()  # check is intager number
                            and valus_in_call[0].count('"')
                            == 2):  # check if string value
                        self.result_handle_attribute.append(
                            ('2 this call is not correct', call))

                elif len_data_type >= 3:
                    if not (valus_in_call[0].replace(
                            ' ', '').isdecimal()  # check is intager number
                            and valus_in_call[1].count('\"') >=
                            2  # check if string value
                            and all(
                                map(lambda value: value.count("\'") >= 2,
                                    valus_in_call[2:])
                            )  # check if all ends argumant is char values
                            ):
                        self.result_handle_attribute.append(
                            ('3> this call is not correct', call))
                else:
                    self.result_handle_attribute.append(
                        ('this call is not correct', call))

        return self.result_handle_attribute

    def __function_and_calls(self) -> None:
        """filter name of the function and put every function with his calls
        """

        function_name = []

        for func in self.functions:
            func_name = re.sub('[^a-zA-Z]', '', func.split(' ')[1])
            function_name.append(func_name)
            self.name_prototype[func_name] = func

        for name in function_name:
            self.function_calls[self.name_prototype[name]] = []

            for call in self.call_function:
                if name in call:
                    self.function_calls[self.name_prototype[name]].append(call)

    def __data_type_function(self, args: list) -> list:
        """function take a arguments and return data type of this arguments

        Args:
            args (list): arguments of the function ( <datType> <nameVaribel> )

        Returns:
            list: data type order
        """

        result = []

        for data_type in args:

            if 'int' in data_type:
                result.append('int')

            elif 'string' in data_type:
                result.append('string')

            elif 'char' in data_type:
                result.append('char')

        return result

    def __check_data_type_order(self, args: list) -> bool:
        """check the order of of data type is correct

        Args:
            args (list): list of data type 

        Returns:
            bool: return True if the order is correct otherwise False
        """

        length = len(args)

        if length == 1 and args == ['int']:
            return True
        elif length == 2 and args == ['int', 'string']:
            return True

        elif length == 3 and args == ['int', 'string', 'char']:
            return True

        elif length >= 4:
            if args[:3] == ['int', 'string', 'char']:
                if all(map(lambda x: x == 'char', args[3:])):
                    return True
        return False

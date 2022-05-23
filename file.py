from functools import wraps
def greeter(func):
    @wraps(func)
    def inner(*args):
        result = "Aloha " + func(*args).title()
        return result
    return inner


def sums_of_str_elements_are_equal(func):
    @wraps(func)
    def inner(*args):
        arg = func(*args).split()
        list = []
        sum_first = 0
        sum_second = 0
        for number in arg:
            if int(number) < 0:
                number = number[1:]
                for digit in number:
                    list.append(-int(digit))
            else:
                for digit in number:
                    list.append(int(digit))
            list.append('*')
        i = 0
        while list[i] != '*':
            sum_first += int(list[i])
            i += 1
        i += 1
        while i < len(list)-1:
            sum_second += int(list[i])
            i += 1
        print(sum_first)
        print(sum_second)
        if sum_first == sum_second:
            return str(sum_first) + ' == ' + str(sum_second)
        return str(sum_first) + ' != ' + str(sum_second)
    return inner

def format_output(*required_keys):
    def inner(func_to_be_decorated):
        def decoration(*args):
            input_dict = func_to_be_decorated(*args)
            output_dict = {}
            for required_index in required_keys:
                temp_list = []
                for required_index_splited in required_index.split("__"):
                    if required_index_splited in input_dict.keys():
                        if input_dict[required_index_splited] == '':
                            input_dict[required_index_splited] = 'Empty value'
                        temp_list.append(input_dict[required_index_splited])
                    else:
                        raise ValueError
                output_dict[required_index] = " ".join(temp_list)
            return output_dict
        return decoration
    return inner


def add_method_to_instance(klass):
    class Dummy(object):
        def foo(self):
            return self.__class__.__name__
    return Dummy.foo

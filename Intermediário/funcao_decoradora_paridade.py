def create_func(func):
    def intern(*args, **kwargs):
        for arg in args:
            is_int(arg)
        result = func(*args, **kwargs)
        print(f'The result is: {result}')
        return result
    return intern

@create_func
def paridade_number(num):
    print(num)
    return num % 2 == 0

def is_int(parameter):
    if not isinstance(parameter, int):
        raise TypeError('The number have to be int')
    
paridade = paridade_number(3)

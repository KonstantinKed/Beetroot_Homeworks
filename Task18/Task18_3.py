from functools import wraps
class TypeDecorators:
    pass

    def to_int(func):
        @wraps(func)
        def wrap(*args,**kwargs):
            try:
                print(func.__name__, 'turns str to int')
                result = int(func(*args,**kwargs))
            except ValueError:
                result = "Impossible operation"
            return result
        return wrap

    def to_str(func):
        @wraps(func)
        def wrap(*args,**kwargs):
            try:
                print(func.__name__,'turns int ot str')
                result = str(func(*args,**kwargs))
            except ValueError:
                result = "Impossible operation"
            return result
        return wrap


    def to_bool(func):
        @wraps(func)
        def wrap(*args,**kwargs):
            try:
                print(func.__name__, 'turns str to bool')
                if args[0] == 'True' or args[0] == 'False':
                    result = bool(func(*args, **kwargs))
                else:
                    result = "Impossible operation"
            except ValueError:
                result = "Impossible operation_error"
            return result
        return wrap

    def to_float(func):
        @wraps(func)
        def wrap(*args,**kwargs):
            try:
                print(func.__name__,'turns str to float')
                result = float(func(*args,**kwargs))
            except ValueError:
                result = "Impossible operation"
            return result
        return wrap

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_str
def do_nothing_2(integer: int):
    return integer

@TypeDecorators.to_bool
def do_something(string: str):
    return string

@TypeDecorators.to_float
def do_something2(string: str):
    return string

print('-----TO INT------')
print(do_nothing('1000'))
print(type(do_nothing('1000')))
print('-----TO STR------')
print(do_nothing_2(1000))
print(type(do_nothing_2(1000)))
print('-----TO BOOL-----')
print(do_something('True'))
print(type(do_something('True')))
print(do_something('True'))
print(type(do_something('True')))
print(do_something('AAA'))
print(type(do_something('AAA')))
print('-----TO FLOAT-----')
print(do_something2('2'))
print(type(do_something2('2')))
print(do_something2('AAA'))
print(type(do_something2('AAA')))
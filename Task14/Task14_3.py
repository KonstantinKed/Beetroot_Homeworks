# Task 3
# Write a decorator `arg_rules` that validates arguments passed to the function.

def arg_rules(type_: type, max_length: int, contains: list):
    def arg_rules_dec(f):
        def wrap(*args, **kwargs):
            f(*args, **kwargs)
            text = {print(f(*args, **kwargs)) for k in args[0].split() if (lambda i, k: i in k in contains) and type(args[0]) is type_ and len(args[0]) <= max_length} # TO BE IMPROVED
            return text
        return wrap
    return arg_rules_dec

@arg_rules(type_= str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan('johndoe05@gmail.com')
create_slogan('S@SH05')
# Task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
import re
def stop_words(words: list):
    def stop_words_dec(f):
        def wrap(*args,**kwargs):
            result = f(*args,**kwargs)
            for word in words:
                #result = result.replace(word, "*")
                result = re.sub(r'\b'+word+r'\b','*', result)
            print(result)
        return wrap
    return stop_words_dec



@stop_words(['pepsi','in', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

create_slogan("Steve")
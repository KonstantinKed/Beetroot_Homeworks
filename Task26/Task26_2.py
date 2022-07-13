class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()
    string = 'f"{ind}:(stack), [queue], {str(item)}{{{((({{[[]]}})))}}}}{"'
    for i in string:
        if i in ['(','{','[']:
            s.push(i)
            print(s)
        elif i in [')','}',']']:
            try:
                if i == ')' and s.peek() == '(' or i == '}' and s.peek() == '{' or i == ']' and s.peek() == '[':
                    s.pop()
                    print(s)
            except IndexError:
                            print('Parentheses were closed before opening')
    if s.is_empty():
        print("String has balanced parentheses")
    else:  # This condition is formal, as IndexError will occur any time it will not find a correct pair
        print('Parentheses were closed before opening_1')

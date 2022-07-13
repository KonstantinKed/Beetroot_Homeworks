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

    def get_from_stack(self, element):
        temp_list = []
        for i in range(s.size()):
            if s.peek() != element:
                temp_list.append(s.pop())
                if s.is_empty():
                    raise ValueError (f'Stack doesn\'t consist searching element "{element}"')
            else:
                s.pop()
                break
        print(temp_list)
        for j in range(len(temp_list)):
            s.push(temp_list.pop())
        return f'Searching element "{element}" was found in Stack'

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()

    s.push(4)
    s.push(3)
    s.push(2)
    s.push('dog')
    s.push(1)
    print(s)
    print(s.get_from_stack('dog'))
    print(s)
    print(s.get_from_stack(1))
    print(s)
    print(s.get_from_stack(4))
    print(s)
    # print(s.get_from_stack('doc'))
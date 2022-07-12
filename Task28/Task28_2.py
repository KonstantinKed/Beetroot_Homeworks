from node import Node


class Stack_UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def push(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def pop(self):  # POP
        if self._head == None:
            return "Stack is empty"
        else:
            pop_elem = self._head
            self._head = self._head.get_next()
            return pop_elem.get_data()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self._head.get_data()

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def __repr__(self):
        representation = "<STACK_from_UNORD_LIST: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()}, "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()

if __name__ == "__main__":
    my_list = Stack_UnorderedList()

    print(my_list.is_empty())
    # my_list.push(31)
    # my_list.push(77)
    # my_list.push(17)
    # my_list.push(93)
    # my_list.push(26)
    # my_list.push(54)
    my_list.push(4)
    my_list.push('dog')
    print(my_list.peek())
    my_list.push(True)
    print(my_list.size())
    print(my_list.is_empty())
    my_list.push(8.4)
    print(my_list)
    print('size is',my_list.size())
    print(my_list.pop())
    print(my_list.pop())
    print(my_list)
    print(my_list.pop())
    print(my_list)
    print(my_list.pop())
    print(my_list)
    print(my_list.pop())


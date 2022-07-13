from node import Node

class Queue_UnorderedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def enqueue(self, item):
        temp = Node(item)
        if self.is_empty():     # if queue is empty we use standard add method
            temp.set_next(self._head)
            self._head = temp
        else:                      # use variation of 'append' method
            current = self._head
            previous = None
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            current.set_next(temp)
            temp.set_next(None)

    def dequeue(self):
        current = self._head
        previous = None
        if self.is_empty():
            return "Queue is empty!!!"
        else:
            while current.get_next() is not None:
                previous = current
                current = current.get_next()
            if previous == None:
                self._head = current.get_next()
            else:
                previous.set_next(None)
                return current.get_data()

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def __repr__(self):
        representation = "<Queue_from_Unordered_List: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()}, "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = Queue_UnorderedList()
    print(my_list.is_empty())  # works!
    my_list.enqueue(4)
    my_list.enqueue('dog')
    my_list.enqueue(True)
    my_list.enqueue('Start')
    print(my_list.size())
    print(my_list)
    print(my_list.dequeue())
    print(my_list.dequeue())
    print(my_list.dequeue())
    print(my_list)
    print(my_list.is_empty())
    print(my_list.dequeue())  # QUESTION!!!!!!! HOW TO REMOVE THE LAST ELEMENT IF PREVIOUS FOR IT IS NONE
    print(my_list)


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def get_from_queue(self, element):
        temp_list = []
        found = False
        for i in range(q.size()):
            if not q.is_empty() and found: # end of search
                break
            if not q.is_empty():
                raise ValueError(f'Stack doesn\'t consist searching element "{element}"')
            temp_var = q.dequeue()
            if temp_var != element:
                temp_list.append(temp_var)
            else:
                found = True
                if q.size()!=0:  # extra check if searching element is the last in queue
                    temp_list.append(q.dequeue())
        print(temp_list)
        temp_list.reverse()
        for j in range(len(temp_list)):
            q.enqueue(temp_list.pop())
        return f'Searching element "{element}" was found in Stack'
    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    print(q.is_empty())
    print(q)
    q.get_from_queue('dog')
    print(q)
    q.get_from_queue(1)
    print(q)

from node import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()
# ________________METHODS DONE AT THE LESSON_________________________
    def find_max(self):
        current = self._head
        maxi = self._head.get_data()
        while current is not None:
            if current.get_data() > maxi:
                maxi = current.get_data()
            current = current.get_next()
        return maxi

    def find_min(self):
        current = self._head
        mini = self._head.get_data()
        while current is not None:
            if current.get_data() < mini:
                mini = current.get_data()
            current = current.get_next()
        return mini

    def remove_first(self):
        self._head = self._head.get_next()

    def remove_last(self):
        current = self._head
        while current.get_next() is not None:
            el = current
            current = current.get_next()
        el.set_next(None)

    def reversed(self):
        prev = None
        current = self._head
        while (current is not None):
            next = current.get_next()
            current.set_next(prev)
            prev = current
            current = next
        self._head = prev

# ____________________HOMETASK___________________________
    def append_meth(self, new_item):  #APPEND METHOD
        new_temp = Node(new_item)
        current = self._head
        while current.get_next() is not None:
            elem = current
            current = current.get_next()
        current.set_next(new_temp)
        new_temp.set_next(None)

    def indexx(self, s_item):
        current = self._head
        found = False
        count_x = -1
        while current is not None and not found:
            if current.get_data() == s_item:
                found = True
            else:
                current = current.get_next()
            count_x += 1
        return count_x

    def pops(self, index):  # POP
        current = self._head
        previous = None
        found = False
        count_x = 0
        while not found:
            if count_x == index:
                element = current
                found = True
            else:
                previous = current
                current = current.get_next()
                count_x += 1
        if previous == None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return element.get_data()

    def insert_meth(self, index_O, new_item):  #INSERT METHOD
        new_temp = Node(new_item)
        current = self._head
        previous = None
        found = False
        count_O = 0
        while not found:
            if count_O == index_O:
                element = current
                found = True
            else:
                count_O += 1
                previous = current
                current = current.get_next()

        if previous == None:  # if index_O is 0 than we have classic add method
            new_temp.set_next(self._head)
            self._head = new_temp
        else:
            new_temp.set_next(current)
            previous.set_next(new_temp)

if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    print('____APPEND______')  # ADD THE ELEMENT TO THE END OF THE LIST
    my_list.append_meth(99)
    print(my_list)
    print('____INDEX___')
    print(my_list)
    print(my_list.indexx(26))
    print(my_list.indexx(100))
    print('____POP___')
    print(my_list)
    print('- 4th element of the list is',my_list.pops(4))
    print(my_list)
    print('- 0 element of the list is', my_list.pops(0))
    print(my_list)
    print('____INSERT___')
    print(my_list)
    my_list.insert_meth(4, 88)
    print(my_list)
    my_list.insert_meth(0, 77)
    print(my_list)
    print('____REVERSED_______')
    print(my_list)
    my_list.reversed() # REVERSED ADDED
    print(my_list)
# Find max and min element in linked list
    print('___________')
    print(my_list)
    print(my_list.find_max())
    print(my_list.find_min())
    my_list.remove_first()
    print(my_list)
    print('___________')
    my_list.remove_last()
    print(my_list)
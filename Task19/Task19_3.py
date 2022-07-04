class Iter_Square:
    def __init__(self, lists: list):
        self.lists = lists

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.lists):
            self.i += 1
            return self.lists[self.i-1]
        else:
            raise StopIteration

    def __getitem__(self, element):
        return self.lists[element]


it = Iter_Square([1,2,3,4,5,6,7,8,9,10])

for i in it:
    print(i, end=' ')
print()
print(it[0])
print(it[4])
# Option 1 Iterator
print('-------Iterator--------')
class With_Index:
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.start = start

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i <= (len(self.iterable)-1):
            self.i +=1
            self.start += 1 # since start can differ than 0
            return self.start-1, self.iterable[self.i-1]
        else:
            raise StopIteration

enum = With_Index(['coke','pepsi','mirinda','scwapse'], 100)
for a in enum:
    print(a, end=' ')
print('\n-------Generator--------')
# Option 2 generator
def with_enum(iterable, start=0):
    n=start
    for iterb in iterable:
        yield (n, iterb)
        n +=1

print(list(with_enum(['coke','pepsi','mirinda','scwapse'], 100)))
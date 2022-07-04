print('-------Iterator--------')
class In_Range:
    def __init__(self, start, end, step=1):
        self.end = end
        self.step = step
        self.start = start

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        if self.i < self.end:
            result = self.i
            self.i += self.step
            return result
        else:
            raise StopIteration

enum = In_Range(0, 30, 5)
res = []
for a in enum:
    res.append(a)
print(res)
print('\n-------Generator--------')
def in_range(start, end, step=1):
    res = start
    while res<end:
        yield res
        res += step
print(list(in_range(0,30,5)))
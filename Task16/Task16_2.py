class Mathematician:
    def __init__(self):
        self.result = []

    def square_num(self, result):
        self.result = list(map(lambda i: i**2, result))
        print(self.result)

    def remove_positives(self, result):
        self.result = [i for i in result if i < 0]
        print(self.result)

    def filter_leaps(self, result):
        self.result = [i for i in result if i % 4 ==0]
        print(self.result)

m = Mathematician()
m.square_num([7, 11, 5, 4])
m.remove_positives([26, -11, -8, 13, -90])
m.filter_leaps([2001, 1884, 1995, 2003, 2020])
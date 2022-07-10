from math import gcd
class Fractions:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def big_com_div(self, a, b):
        if a == 1:
            return a, b
        else:
            a, b = int(a/gcd(a,b)), int(b/gcd(a,b))
            if b == 1:
                return a
            else:
                return a, b

    def __add__(self, other):
        nn = self.n * other.d + other.n * self.d
        dd = self.d * other.d
        return self.big_com_div(nn,dd)

    def __sub__(self, other):
        nn = self.n * other.d - other.n * self.d
        dd = self.d * other.d  #
        return self.big_com_div(nn,dd)

    def __mul__(self, other):
        nn = self.n * other.n
        dd = self.d * other.d  #
        return self.big_com_div(nn,dd)

    def __truediv__(self, other):
        if other.n == 0 or other.d == 0:
            raise ZeroDivisionError ("can't divide on 0")
        nn = self.n * other.d
        dd = self.d * other.n
        return self.big_com_div(nn,dd)

f1 = Fractions(1, 2)
f2 = Fractions(1, 4)
print((f1+f2))
print((f1-f2))
print((f1*f2))
print((f1/f2))
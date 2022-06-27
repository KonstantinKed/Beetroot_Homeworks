from fractions import Fraction

class Fractions:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError ("can't divide on 0")
        return self.x / other.x

f1 = Fractions(1/2)
f2 = Fractions(1/4)
print(Fraction(f1+f2))
print(Fraction(f1-f2))
print(Fraction(f1*f2))
print(Fraction(f1/f2))
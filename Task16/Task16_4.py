class CustomException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def input(self, lists: list):
        if not isinstance(lists, list):
            raise CustomException("You enter wrong variable type")
        lists2 = []
        for i in lists:
            lists2.append(i ** 2)
        return lists2

    def divide(self, x, y):
        if y == 0:
            raise CustomException("Can not divide on zero")
        return x / y

    def __str__(self):
        with open('log.txt', "a") as f:
            f.write(f'{self.msg}\n')
        return self.msg


a = CustomException("foo")

print(a.input([1,2,3,4]))
# print(a.input((1,2,3,4)))  #
print(a.divide(2, 0))
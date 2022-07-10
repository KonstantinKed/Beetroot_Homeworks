# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
import re
class Email:
    def __init__(self):
        pass


    def validate(self, email):
        if re.match("^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
            return (f"{email} -- is correct syntax in email address")
        else:
            return (f"{email} -- is Wrong syntax in email address")



em = Email()

print(em.validate(("abc..def@mail.com")))
print(em.validate(("abc-@mail.com")))
print(em.validate((".abc@mail.com")))
print(em.validate(("abc#def@mail.com")))
print(em.validate(("abc.def@mail.c")))
print(em.validate(("abc.def@mail#archive.com")))
print(em.validate(("abc.def@mail")))
print(em.validate(("abc.def@mail..com")))
print(em.validate(("abc.def@mail.com")))
print(em.validate(("abc.def@mail.org")))
print(em.validate(("abc.def@mail-archive.com")))  # counts as wrong =(  need some check in regex list
print(em.validate(("abc.def@mail.cc")))
print(em.validate(("abc_def@mail.com")))
print(em.validate(("abc@mail.com")))
print(em.validate(("abc.def@mail.com")))
print(em.validate(("abc-d@mail.com")))





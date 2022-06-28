# Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
# passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.
import re
class Email:
    def __init__(self, email):
        self.email = email

    @classmethod
    def validate(Email, email):
        if re.match("^[a-z0-9]+[\._-]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email):
            return (f"{email} -- is correct syntax in email address")
        else:
            return (f"{email} -- is Wrong syntax in email address")


print(Email.validate(("abc..def@mail.com")))
print(Email.validate(("abc-@mail.com")))
print(Email.validate((".abc@mail.com")))
print(Email.validate(("abc#def@mail.com")))
print(Email.validate(("abc.def@mail.c")))
print(Email.validate(("abc.def@mail#archive.com")))
print(Email.validate(("abc.def@mail")))
print(Email.validate(("abc.def@mail..com")))
print(Email.validate(("abc.def@mail.com")))
print(Email.validate(("abc.def@mail.org")))
print(Email.validate(("abc.def@mail-archive.com")))  # counts as wrong =(  need some check in regex list
print(Email.validate(("abc.def@mail.cc")))
print(Email.validate(("abc_def@mail.com")))
print(Email.validate(("abc@mail.com")))
print(Email.validate(("abc.def@mail.com")))
print(Email.validate(("abc-d@mail.com")))





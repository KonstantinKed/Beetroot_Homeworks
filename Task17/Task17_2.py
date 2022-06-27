class Library:
    def __init__(self, l_name):
        self.l_name = l_name
        self.books = []
        self.authors = []

    def new_book(self, book, year, author):
        self.book = book.name
        self.year = year.year
        self.author = author
        self.books.append(book)   # append the instance of book
        self.authors.append(self.author)

    def __str__(self):
        lib_books=[]
        for bk in self.books:
            lib_books.append(bk.name)
        return f'{self.l_name}: {lib_books}'

    def group_by_author(self, author):
        auth_book = []
        for book in self.books:
            if book.author == author:
                auth_book.append(book.name)
        return f'{author}: {auth_book}'

    def group_by_year(self, year):
        year_book = []
        for book in self.books:
            if book.year == year:
                year_book.append(book.name)
        return f'{year}: {year_book}'

class Book:
    book_amount = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author   # author is an instance of Author class!
        Book.book_amount += 1

    def __str__(self):
        return (f'Name: {self.name}, Author: {self.author}, Year of issue: {self.year}, Total books: {self.book_amount}')


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.book = [] # list of books from author

    def add_book_auth(self, auth_book):
        self.book.append(auth_book)

    def __str__(self):
        return (f'Author: {self.name}, From: {self.country}, Author bithyear: {self.birthday}, Available books: {self.book}')



auth = Author('Uval Noi Harari', 'Izrael', 1976)
auth2 = Author('Thomas Harris', 'USA', 1940)
auth3 = Author('Ivan Vakarchuk', 'Ukraine', 1947)
auth4 = Author('Stephen Hawking', 'UK', 1942)
bk1 = Book('Sapiens', 2018, auth.name)
bk2 = Book('Homo Deus', 2019, auth.name)
bk3 = Book('21 lessons for 21 century', 2020, auth.name)
bk4 = Book('Red Dragon', 2018, auth2.name)
bk5 = Book('Silence of Lambs', 2019, auth2.name)
bk6 = Book('Hannibal', 2020, auth2.name)
bk7 = Book('Quantum Mechanic', 2018, auth3.name)
bk8 = Book('Brief Answers to Big Questions', 2019, auth4.name)
auth.add_book_auth(bk1.name)
auth.add_book_auth(bk2.name)
auth.add_book_auth(bk3.name)
auth2.add_book_auth(bk4.name)
auth2.add_book_auth(bk5.name)
auth2.add_book_auth(bk6.name)
auth3.add_book_auth(bk7.name)
auth4.add_book_auth(bk8.name)
print('_______library______')
l1 = Library('Vernadskogo')
l2 = Library('Shevchenko Univeristy')
l1.new_book(bk1, bk1, bk1.author)
l1.new_book(bk2, bk2, bk2.author)
l1.new_book(bk3, bk3, bk3.author)
l1.new_book(bk4, bk4, bk4.author)
l1.new_book(bk5, bk5, bk5.author)
l1.new_book(bk6, bk6, bk6.author)
l1.new_book(bk7, bk7, bk7.author)
l2.new_book(bk7, bk7, bk7.author)
l2.new_book(bk8, bk8, bk8.author)
l2.new_book(bk3, bk3, bk3.author)  # add a book to several libraries
print(l1)
print(l2)
print('_______author______')
print(auth)
print(auth2)
print(auth3)
print(auth4)
print('_______books______')
print(bk1)
print(bk2)
print(bk3)
print(bk4)
print(bk5)
print(bk6)
print(bk7)
print(bk8)
print('_______group_by_author______')
print('________',l1.l_name,'_______')
print(l1.group_by_author(auth.name))
print(l1.group_by_author(auth2.name))
print('________',l2.l_name,'_______')
print(l2.group_by_author(auth3.name))
print(l2.group_by_author(auth4.name))
print('_______group_by_year______')
print(l1.group_by_year(2018))
print(l1.group_by_year(2019))
print(l1.group_by_year(2020))
print(l2.group_by_year(2018))
print(l2.group_by_year(2019))
print(l2.group_by_year(2020))
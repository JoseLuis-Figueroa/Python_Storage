##############################################################################
# Understanding inheritance
##############################################################################
# The inheritance is used to order the classes when there are repeated 
# attributes and it gives better flow to the code

# Publication is the base|father of the all the classes
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

# This class is a child and it is used to Magazine and Newspaper classes
class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period


# Book class is using Publication class directly as title and price attributes
# are used and this class
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

# Magazine and Newspaper classes used the Periodical class due to they have 
# the same attributes
class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("My Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)


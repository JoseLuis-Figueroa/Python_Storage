##############################################################################
# Using composition to build complex objects
##############################################################################
# Composition is another way to organize classes as Inheritance. Composition
# means that an object knows another object, and explicitly delegates some 
# tasks to it. Composition works when a class uses another one as object.

# Book class contains as an attribute the Author class
class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    # This method contains as an attribute the Chapter class
    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # Magic method
    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

# Author constructor
auth = Author("Leo", "Tolstoy")
# Book constructor contains auth object as an attribute
b1 = Book("War and Peace", 39.0, auth)

# Method addchapter uses the Chapter book as object
b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.author)
print(b1.title)
print(b1.getbookpagecount())
##############################################################################
# Using class-level and static methods
##############################################################################
class Book:
    # TODO: propierties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore propierties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # Instance methods receive a specific object instance as an argument and
    # operate on data specific to that object instance
    def SetTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, book_type):
        self.title = title
        if (not book_type in Book.BOOK_TYPES):
            raise ValueError(f"{book_type} is not a valid book type")
        else:
            self.book_type = book_type

# TODO: access the class attribute
print("Book types: ", Book.getbooktypes())

# TODO: Create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")
b3 = Book("Title 2", "PAPERB")

# TODO: Use the static method to access a singleton object 
thebooks = Book.getbooklist()
thebooks.append(b1.book_type)
thebooks.append(b2.book_type)
print(thebooks)

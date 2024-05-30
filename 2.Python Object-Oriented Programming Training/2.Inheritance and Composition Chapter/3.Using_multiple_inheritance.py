##############################################################################
# Multiple inheritance 1 at a class
##############################################################################
# It is not recommened way to use the multiple inheritance
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

# Class C is child of classes A and B
class C(B, A):
    def __init__(self):
        super().__init__()

    # Be careful when uses 2 Base class as if they define the same attribute
    # Class will take the first defined class "B"
    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)

c = C()
c.showprops()
# __mro__ function provides the order of the classes
print(C.__mro__)
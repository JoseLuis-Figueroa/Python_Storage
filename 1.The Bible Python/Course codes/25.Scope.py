#####################################
############## Scope ################
#####################################

# global variables
a = 100

# Functions
def f1():
    b = a + 50
    print(b)

def f2():
    #Create a local function called a into this function
    a = 50
    print(a)

# call functions
f1()
f2()

#Print the global variable called a
print(a)

####################################################
################### Read Files #####################
####################################################

#Use open() function to open the file
f = open("ReadFile.txt","r")
#Use read() function to read the file
print(f.read())
#Note: You can specify how many characters you want to return on 
#read() function

print("")

#Use readline() function to read a line
f = open("ReadFile.txt","r")
print(f.readline())

print("")

#Use a for to read the file line by line
f = open("ReadFile.txt","r")
for x in f:
    print(x)

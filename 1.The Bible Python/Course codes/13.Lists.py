#############################################
############   List  ########################
#############################################

#create list A
A = [5, 98, 8, 15]
print(A)

#Add new element
A = A + [1]
print(A)

#Add string
A = A + ["A"]
print(A)

#Add some strings
A = A + list("ABC")
print(A)

#Add some numbers
A = A + [1, 2, 3]
print(A)

#Add a list of elements
A = A + [[5,7,8]]
print(A)

#Another way to add elements
A.append([10,2])
print(A)

#New list B
B = [7,5,3]
print(B)

#Insert data into different place of the list
B.insert(2,55)
print(B)

#Removo data
B.remove(7)
print(B)

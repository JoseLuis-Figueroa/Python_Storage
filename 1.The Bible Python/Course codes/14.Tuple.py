#############################
########  Tuple  ############
#############################

#create a tuple
Our_tuple = 1,2,3,"A","B","C"
print(type(Our_tuple))
print(Our_tuple)

#Our_tuple[2] = 10
#print(Our_tuple)

#Note: The tuple can't be change once it was created, so it is the difference with the list
#This gets an error if I try to change a value 

#create a list
Our_list = [1,2,3,"A"]
print(type(Our_list))
print(Our_list)

Our_list[2] = 10
print(Our_list)

#Convert list to tuple
A = [1,3,5]
print(type(A))
A= tuple(A)
print(type(A))

#Conclution
#The tuple is used to keep data that can't be changed



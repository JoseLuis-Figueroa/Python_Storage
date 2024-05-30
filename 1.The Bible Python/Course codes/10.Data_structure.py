################################################
############    Data Structure   ###############
################################################

#list of data
our_list = [27, 8, 9, 10, -4]
print(our_list)
print(type(our_list))

#list of data with different types
jack = ["A","B","C", 1, 2, 3, "Do", True]
print(jack)
print(jack[2])

#print a grup of data
x=jack[:jack.index("C")+1]
print(x)

#list of data with lists included
new_list=[1,2,[3,4,5,],6]
print(new_list)
#print list
y=new_list[2]
print(y)
#print number of the list
y1=new_list[2][1]
print(y1)

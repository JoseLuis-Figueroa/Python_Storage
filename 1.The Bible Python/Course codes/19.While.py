#####################################
#########  While loops  #############
#####################################

#Variables
number = 1
L = []

while number <= 10:
    print(number)
    #The next line is equal to number = number +1
    number+=1

while len(L) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry list is full")
print(L)

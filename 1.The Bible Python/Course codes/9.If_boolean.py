################################################
#########If with boolean conditions#############
################################################
num1=int(input("Give me the first number "))
num2=int(input("Give me the second number "))
num3=int(input("Give me the third number "))

if num1>num2 and num1>num3:
    print("First number is higher than other numbers")
elif num2>num1 and num2>num3:
    print("Second number is higher than other numbers")
elif num3>num1 and num3>num2:
    print("Third number is higher than other numbers")
else:
    print("Any number is higher that other numbers")
    

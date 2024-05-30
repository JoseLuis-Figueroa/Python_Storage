# Dictionary Comprehension

# Creating a dictionary using dictionary comprehension and a list
dict = {num: num**2 for num in [1,2,3,4,5]}
print(dict)

# Creating a dictionary using dictionary comprehension and 2 strings
str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0,len(str1))}
print(combo)

# Conditional logic with dictionaries
num_list = [1,2,3,4]
dict2 = {num:("even" if num%2 == 0 else "odd") for num in num_list}
print(dict2)
# Dictionary 

# Delete a specific element from a dictionary
instructor = {'name': "Colt", 'dog': True, 'number': 4, 'message': "No"}
print("Instructor contains: ",instructor )
print("\n")
instructor.pop('dog')
print("Delete dog: ",instructor)

# Delete a random element from a dictionary
instructor.popitem()
print(instructor)

# Update a dictionary with another one
manager = {'city': "Zacatecas"}
print("manager contains:", manager)
manager.update(instructor)
print("Manager is updated:",manager)

manager['name'] = "Julio"
print(manager)
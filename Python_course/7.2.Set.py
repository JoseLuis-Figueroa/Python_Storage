# Sets
cities = ["Los Angeles", "Aguascalientes", "Madrid", "Brugge", "Paris", "Madrid"]
# To count unique cities (Set count the unique values)
print(len(set(cities)))
# Convert from list -> set -> list to get a list of uniques
print(list(set(cities)))

# Teacher two classes
math_students = {"Matthew", "Carlos", "James", "Jane"}
biology_students = {"James", "Oliver", "Carlos", "John", "Ariana"} 

# To generate a set with all my unique student
print(math_students | biology_students)

# To generate a set with student who are in both courses
print(math_students & biology_students)


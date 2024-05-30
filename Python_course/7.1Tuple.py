#TUPLES
#Tuples are commonly used for unchanging data
months = ('January', 'February', 'March', 'April', 'May')

for month in months:
	print(month)
	
i = len(months)-1
while i >= 0:
	print(months[i])
	i -= 1


#Tuples can be used as keys in dictionaries
locations = {
	(35.68, 39.69): "Tokyo Office",
	(40.71, 74.06): "New York Office",
	(37.77, 122.41): "San Francisco Office"
}
print(locations)

# Some dictionary methods like .items() return tuples
cat = {"name": "biscuit", "age": 0.5, "favorite_toy": "my chapstick"}
cat.items()
print(cat)
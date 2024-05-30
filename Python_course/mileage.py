# mileage
print("How many kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 4)
print("Your %s km ride was %s mi" % (kms, miles))
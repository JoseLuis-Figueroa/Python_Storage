#Function Random
import random

#variables
health = 50
difficulty = 1

#potion operation
potion_health = int(random.randint(25,50)/difficulty)

#Adder
health = health + potion_health

print(health)

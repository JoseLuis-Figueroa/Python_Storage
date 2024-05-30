# Rock...Paper...Scissors
import random

print("\nWelcome to rock...paper...scissors\n\n")
result = ''

while result == 'Draw' or result == '':

	player = input("Enter player 1's choice:\n").lower()
	rand_num = random.randint(0,2)
	options = ['rock', 'paper', 'scissors']
	computer = options[rand_num]
	print("Computer choice:\n%s" % computer)
	
	print("\nSHOOT!\n")

	if (player == 'rock' and computer == 'rock') or (player == 'paper' and computer == 'paper') or (player == 'scissors' and computer == 'scissors'):
		print("Draw!\n")
		print("Enter new choices!")
		result = 'Draw'
	elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
		print("Player wins!\n")
		break
	elif (computer == 'rock' and player == 'scissors') or (computer == 'paper' and player == 'rock') or (computer == 'scissors' and player == 'paper'):
		print("computer wins!\n")
		break
	else:
		print("Choices not valid\n")
		print("Enter new choices!")
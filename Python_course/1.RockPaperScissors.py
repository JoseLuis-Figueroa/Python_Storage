# Rock...Paper...Scissors
print("\nWelcome to rock...paper...scissors\n\n")
result = ''

while result == 'Draw' or result == '':

	player1 = input("Enter player 1's choice:\n")
	player2 = input("Enter player 2's choice:\n")
	print("\nSHOOT!\n")

	if (player1 == 'rock' and player2 == 'rock') or (player1 == 'paper' and player2 == 'paper') or (player1 == 'scissors' and player2 == 'scissors'):
		print("Draw!\n")
		print("Enter new choices!")
		result = 'Draw'
	elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'paper'):
		print("Player 1 wins!\n")
		break
	elif (player2 == 'rock' and player1 == 'scissors') or (player2 == 'paper' and player1 == 'rock') or (player2 == 'scissors' and player1 == 'paper'):
		print("Player 2 wins!\n")
		break
	else:
		print("Choices not valid\n")
		print("Enter new choices!")

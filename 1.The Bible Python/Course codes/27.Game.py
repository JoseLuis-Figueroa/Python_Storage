############### Tic Tac Toe Game #######################

#Create the nine spaces at a list using an internal For
board = [" " for i in range(9)]


################### Function ############################

#Function to draw the board
def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5]) 
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print("")
    print(row1)
    print(row2)
    print(row3)
    print("")

#Function to perform the movement
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print("Your turn player {}".format(number))

    choice = int(input("Enter your move (1-9): "))
    if board[choice -1] == " ":
        board[choice -1] = icon
    else:
        print("")
        print("This space is taken!")

#Function to review the winner
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
       
       


##################### Main ##############################
while True:
    print_board()
    player_move("X")
    print_board()
    player_move("O")
    

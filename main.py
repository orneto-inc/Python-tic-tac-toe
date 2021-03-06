board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

#_______ GLOBAL VARIABLE _________
game_still_going = True
winner = None
current_player = "X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])



def play_game():

    display_board()
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()
        flip_player()

    if winner== "X" or winner == "O":
        print(winner + " WON.")
    elif winner == None:
        print("Tie")    
   

def handle_turn(current_player):
    print(current_player +"'s Turn")
    position = input("Enter Your Desired Position From 1 to 9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] :
            position = input("Please Enter a valid number which is less than or equal to 9 : ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else :
            print("That place is Taken, Please Choose Other Spot")
    

    board[position] = current_player
    display_board()



def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    
    if row1 or row2 or row3:
        game_still_going = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    
    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return
    
def check_diagonals():
    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"
    
    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    
    return
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

play_game()
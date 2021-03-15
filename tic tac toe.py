

board=["*","*","*",
       "*","*","*",
       "*","*","*"]

current_player="X"
gameisgoing = True
winner = None

def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn():
    position=int(input("Enter the number of position from 0 to 8:"))
    if position < 8:
        board[position] = current_player

    if position > 8:
        position = int(input("Choose a random position from 0 to 8:"))

    board[position] = current_player






def swap_trun():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"




def check_the_winner():
    global  winner
    rowWinner=check_row()
    colWinner=check_coloum()
    diagWinner=check_diagonal()
    check_tie()

    if rowWinner:
        winner=rowWinner
    elif colWinner:
        winner=colWinner
    else:
        winner=diagWinner


def check_row():
    global gameisgoing
    row1=board[0] == board[1] == board[2] != "*"
    row2=board[3] == board[4] == board[5] != "*"
    row3=board[6] == board[7] == board[8] != "*"

    if row1 or row2 or row3:
        gameisgoing= False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]



def check_coloum():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "*"
    col2 = board[1] == board[4] == board[7] != "*"
    col3 = board[2] == board[5] == board[8] != "*"

    if col1 or col2 or col3:
        gameisgoing = False

    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[5]

def check_diagonal():
    global gameisgoing
    diag1 = board[0] == board[4] == board[8] != "*"
    diag2 = board[2] == board[4] == board[6] != "*"


    if diag1 or diag2:
        gameisgoing = False

    if diag1:
        return board[0]
    elif diag2:
        return board[4]


def check_tie():
    global gameisgoing
    if "*" not in board:
        gameisgoing= False
        print("Match is Tied")





def play():
    while gameisgoing:
        show_board()
        handle_turn()
        swap_trun()
        check_the_winner()

        if winner == "X":
            print("X is the winner")
        elif winner == "O":
            print("O is the winner")



play()





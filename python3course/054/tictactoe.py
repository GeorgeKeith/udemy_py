board = [" "]*9
conversion = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8}

def init_board():
    for i in range(0,9):
        board[i] = " "

def printBoard():
    print("   |   |   ")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("   |   |   ")

def move(xo):
    prompt = "Enter square number for {}: ".format(xo)
    while True:
        c = input(prompt)
        if len(c) != 1:
            prompt = "Enter a single digit for {}: ".format(xo)
        elif not c in "123456789":
            prompt = "Invalid input, use digit 1-9 for {}: ".format(xo)
        elif board[conversion[c]] != ' ':
            prompt = "Invalid move, pick unused square for {}: ".format(xo)
        else:
            board[conversion[c]] = xo
            break

def game_won():
    if board[6] != ' ' and board[6] == board[7] == board[8]:
        return True
    if board[3] != ' ' and board[3] == board[4] == board[5]:
        return True
    if board[0] != ' ' and board[0] == board[1] == board[2]:
        return True

    if board[6] != ' ' and board[6] == board[3] == board[0]:
        return True
    if board[7] != ' ' and board[7] == board[4] == board[1]:
        return True
    if board[8] != ' ' and board[8] == board[5] == board[2]:
        return True

    if board[6] != ' ' and board[6] == board[4] == board[2]:
        return True
    if board[8] != ' ' and board[8] == board[4] == board[0]:
        return True
    return False

def play_a_game():
    init_board()
    xo = "X"
    for i in range(0,9):
        printBoard()
        move(xo)
        if game_won():
            print("Congradulations, you won.")
            break
        if xo == 'X':
            xo = 'O'
        else:
            xo = 'X'
    print("Game over. It was a draw.")


while True:
    c = input("Do you want to play a game? ")
    if c.lower() == "y":
        play_a_game()
    else:
        break
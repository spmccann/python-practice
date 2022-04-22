import random

blank = " "
x = "X"
o = "O"
board = [blank] * 9


def outcome():
    top = "".join(board[:3])
    middle = "".join(board[3:6])
    bottom = "".join(board[6:])
    left = board[0] + board[3] + board[6]
    center = board[1] + board[4] + board[7]
    right = board[2] + board[5] + board[8]
    l_diag = board[2] + board[4] + board[6]
    r_diag = board[0] + board[4] + board[8]
    cases = [top, middle, bottom, left, center, right, l_diag, r_diag]
    player_win = "XXX"
    computer_win = "OOO"
    if player_win in cases:
        print("You got Tic Tac Toe. You win!")
        return True
    elif computer_win in cases:
        print("Computer got Tic Tac Toe. You lose.")
        return True
    elif blank not in board:
        print("Game over. There's no more open squares. It's a tie.")
        return True
    else:
        return False


def computer_move():
    options = []
    for count, square in enumerate(board):
        if square == blank:
            options.append(count)
    choice = random.choice(options)
    board[choice] = o


def player_move():
    player = input("Where would you like to place an 'X' (0-8)? ")
    if int(player) not in range(0, 9):
        print("That number is invalid. Please select an open square using numbers 0-8")
        player_move()
    elif board[int(player)] == blank:
        board[int(player)] = x
    else:
        print("That square has already been marked. Please pick an empty square")
        player_move()


def display_board():
    return print(f"""
               {board[0]} | {board[1]} | {board[2]}
              -----------
               {board[3]} | {board[4]} | {board[5]}
              -----------
               {board[6]} | {board[7]} | {board[8]}
           """)


# New game
print("Hello and welcome to a new game of Tic Tac Toe")
print(f"""
            0 | 1 | 2
           -----------
            3 | 4 | 5
           -----------
            6 | 7 | 8
        """)
player_move()
game_over = False
turn = False

while not game_over:
    if not outcome():
        if turn:
            player_move()
            display_board()
            turn = False
        else:
            computer_move()
            print("------------------------------------------\nComputer has moved. It's your turn.")
            display_board()
            turn = True
    else:
        game_over = True
        display_board()

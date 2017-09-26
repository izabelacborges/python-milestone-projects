def print_example() :
    print("The board positions is as follow: \n")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\nYou'll choose your marker next, and on \nyour turn you'll choose a position from 1 to 9. \nYour marker will be placed on the position you chose.")

def init_board() :
    return [ " ", " ", " ", " ", " ", " ", " ", " ", " " ]

def choose_marker() :
    player1 = input("Choose your marker: 'X' or 'O' ? ")
    player2 = "O" if player1 == "X" else "X"
    return [player1, player2]

def ask_for_position(board) :
    position = int(input("Choose a position ranging from 1 to 9: "))
    if not check_position(board, position) :
        return ask_for_position(board)

    return position

def check_position(board, position):
    if board[position-1] != " " or position > 9:
            print("You entered an invalid position.")
            return False

    return True

def place_marker(board, player, position) :
    board[position-1] = player

    return board

def print_board(board) :
    print("\n {b[0]} | {b[1]} | {b[2]} ".format(b = board))
    print("---+---+---")
    print(" {b[3]} | {b[4]} | {b[5]} ".format(b = board))
    print("---+---+---")
    print(" {b[6]} | {b[7]} | {b[8]} \n".format(b = board))

def check_game_over(board) :
    if won(board) :
        return True
    elif tied(board) :
        return True

    return False

def won(board) :
    if crossed_line(board) or crossed_column(board) or crossed_diagonal(board) :
        return True

    return False

def crossed_line(board):
    for i in range(7) :
        if i%3 == 0 :
            if board[i] != " " and (board[i] == board[i+1] and board[i+1] == board[i+2]) :
                print("The player {pl} WON the game!".format(pl = board[i]))
                return True

    return False

def crossed_column(board):
    for i in range(3) :
        if  board[i] != " " and (board[i] == board[i+3] and board[i+3] == board[i+6]) :
            print("The player {pl} WON the game!".format(pl = board[i]))
            return True

    return False

def crossed_diagonal(board):
    if (board[0] == board[4] and board[4] == board[8] or board[2] == board[4] and board[4] == board[6]) and board[4] != " " :
        print("The player {pl} WON the game!".format(pl = board[i]))
        return True

    return False

def tied(board) :
    for i in range(9):
        if board[i] == " ":
            return False

    print("The game is tied!")
    return True

# def tied_line(board):


# def tied_column(board):


# def tied_diagonal(board):


def game() :
    print_example()
    board = init_board()
    players = choose_marker()
    count_player = 0

    while not check_game_over(board) :
        position = ask_for_position(board)
        board = place_marker(board, players[count_player%2], position)
        print_board(board)
        count_player += 1

    again = input("Do you wanna play again? y/n\n")
    if again == "y" :
        game()


game()

class tictactoe_game :

    def print_example() :
        print("The board positions is as follow: \n")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("\nYou'll choose your marker and on \nyour turn you'll choose a position.")

    def init_board() :
        return [ " ", " ", " ", " ", " ", " ", " ", " ", " " ]

    def choose_marker() :
        player1 = input("Choose your marker: 'X' or 'O' ?")
        player2 = "O" if player1 == "X" else "X"
        return [player1, player2]

    def place_marker( board, player, position ) :
        board[position-1] = player

    def print_board( board ) :
        print(" {0} | {1} | {2} ".format(b = board))
        print("-----------")
        print(" {3} | {4} | {5} ".format(b = board))
        print("-----------")
        print(" {6} | {7} | {8} ".format(b = board))

    # def check_turn() :



    def won(board) :
        for i in range(7) :
            if (i%3 == 0 and board[i] == board[i+1] == board[i+2])  :
                return True
        for i in range(3) :
            if ()

    # def tied() :


    # def lost() :


    def game() :
        print_example()
        board = init_board()
        players = choose_marker()


    print_example()

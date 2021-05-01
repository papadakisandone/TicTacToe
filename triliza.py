board = [
    # 0    1    2
    [" ", " ", " "],  # 0
    [" ", " ", " "],  # 1
    [" ", " ", " "]  # 2

]


def check_win(player):
    game = "play"
    # orizodios elegxos
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2]) and board[0][0] != " ":
        print("The winner is the Player " + player)
        game = "end_game"
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]) and board[1][0] != " ":
        print("The winner is the Player " + player)
        game = "end_game"
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2]) and board[2][0] != " ":
        print("The winner is the Player " + player)
        game = "end_game"
    # kathetos elegxos
    elif (board[0][0] == board[1][0] and board[1][0] == board[2][0]) and board[0][0] != " ":
        print("The winner is the Player " + player)
        game = "end_game"
    elif (board[0][1] == board[1][1] and board[1][1] == board[2][1]) and board[0][1] != " ":
        print("The winner is the Player " + player)
        game = "end_game"
    elif (board[0][2] == board[1][2] and board[1][2] == board[2][2]) and board[0][2] != " ":
        print("The winner is the Player " + player)
        game = "end_game"
    # diagonios elegxos
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != " ":
        print("The winner is the Player " + player)
        game = "end_game"
    elif (board[0][2] == board[1][1] and board[1][1] == board[2][0]) and board[0][2] != " ":
        print("The winner is the Player " + player)
        game = "end_game"

    return game


def print_board():
    print("    0   1   2")
    print("  +---+---+---+")
    print("0 | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | 0")
    print("  +---+---+---+")
    print("1 | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | 1")
    print("  +---+---+---+")
    print("2 | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | 2")
    print("  +---+---+---+")
    print("    0   1   2")


def main():
    player = "O"

    for times in range(9):  # run 9 times as the squares
        print_board()

        # switch  players
        if player == "X":
            player = "O"
        else:
            player = "X"

        print("Now Player " + player + " is playing")

        row = True
        col = True
        player_row = " "  # gia na mporei o elegxos if gia keno box na dei tis metavlites, check for empty box
        player_col = " "  # gia na mporei o elegxos if gia keno box na dei tis metavlites

        while True:  # check the inputs

            while row:  # check row number
                player_row = int(input("Choose Row: "))
                if player_row < 0 or player_row > 2:
                    print("Choose row from 0-2")
                else:
                    row = False

            while col:  # check column number
                player_col = int(input("Choose Column: "))
                if player_col < 0 or player_col > 2:
                    print("Choose column from 0-2")
                else:
                    col = False

            if board[player_row][player_col] != " ":  # if choose non empty box
                print("Choose an empty box")
                row = True  # gia na ksana dialexei box
                col = True  # gia na ksana dialexei box
            else:
                board[player_row][player_col] = player  # add symbol of the player in that specific box
                break  # an ola pane kala

        # check for winner
        game = check_win(player)
        if game == "end_game":
            break

    else:  # for
        print("\n The Game is Draw!!!")  # loop run 9 times with no winner
        print_board()


main()

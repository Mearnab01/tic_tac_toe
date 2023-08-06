# This is project 10.
# Tic-Tac-Toe game


# Global variables
board = [' ' for _ in range(9)] 
current_player = 'X'
game_still_running = True
winner = None


def display_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def play_game():
    display_board()

    while game_still_running:
        handle_turn(current_player)
        check_game_over()
        flip_player()

    if winner == 'X' or winner == 'O':
        print(f"Congratulations! {winner} won the game!")
    else:
        print("It's a tie!")


def handle_turn(player):
    print(f"\n{player}'s turn.")
    position = input("Choose a position from 1-9: ")

    valid_position = False
    while not valid_position:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == ' ':
            valid_position = True
        else:
            print("That position is already filled. Choose another position: ")

    board[position] = player
    display_board()


def check_game_over():
    check_winner()
    check_tie()


def check_winner():
    global winner

    # Check rows
    row_winner = check_rows()
    if row_winner:
        winner = row_winner
        return

    # Check columns
    column_winner = check_columns()
    if column_winner:
        winner = column_winner
        return

    # Check diagonals
    diagonal_winner = check_diagonals()
    if diagonal_winner:
        winner = diagonal_winner
        return


def check_rows():
    global game_still_running

    row1 = board[0] == board[1] == board[2] != ' '
    row2 = board[3] == board[4] == board[5] != ' '
    row3 = board[6] == board[7] == board[8] != ' '

    if row1:
        game_still_running = False
        return board[0]
    elif row2:
        game_still_running = False
        return board[3]
    elif row3:
        game_still_running = False
        return board[6]

    return None



def check_columns():
    global game_still_running

    column1 = board[0] == board[3] == board[6] != ' '
    column2 = board[1] == board[4] == board[7] != ' '
    column3 = board[2] == board[5] == board[8] != ' '

    if column1 or column2 or column3:
        game_still_running = False
        return board[0]  # Return board[0] to current_player

    return None


def check_diagonals():
    global game_still_running

    diagonal1 = board[0] == board[4] == board[8] != ' '
    diagonal2 = board[2] == board[4] == board[6] != ' '

    if diagonal1 or diagonal2:
        game_still_running = False
        return board[4]  # Return board[4] to current_player

    return None


def check_tie():
    global game_still_running

    if ' ' not in board:
        game_still_running = False
        return True

    return False


def flip_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


# Start the game
play_game()

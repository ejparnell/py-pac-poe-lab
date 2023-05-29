def main():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    turn = 1
    move_count = 0
    winner = 0
    init()
    while winner == 0 and move_count != 9:
        turn_order(turn)
        player_move = get_move()
        if check_move(board, player_move, turn):
            turn *= -1
            move_count += 1
            winner = check_winner(board, winner)
            render_board(board)
        print_winner(winner, move_count)


def init():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print("----------------------\nLet's play Py-Pac-Poe!\n----------------------")
    render_board(board)


def render_board(board):
    column_list = f"\n    A     B     C"
    row1 = f"1)  {board[0]}  |  {board[1]}  |  {board[2]}"
    row2 = f"2)  {board[3]}  |  {board[4]}  |  {board[5]}"
    row3 = f"3)  {board[6]}  |  {board[7]}  |  {board[8]}\n"
    print(column_list)
    print(row1)
    print(row2)
    print(row3)


def turn_order(turn):
    player1 = "X"
    player2 = "O"
    if turn == 1:
        print(f"It is {player1}'s turn\n")
    else:
        print(f"It is {player2}'s turn\n")


def print_winner(winner, move_count):
    if winner == 0 and move_count == 9:
        print(f"Sorry No One Wins - CAT Game")
    elif winner == 1:
        print(f"Congrats! X has won")
    elif winner == -1:
        print(f"Congrats! O has won")


def get_move():
    player_input_col = input("Please enter a column: ")
    player_input_row = input("Please enter a row: ")
    # if player_input_col != "a" or player_input_col != "b":
    if player_input_col == "a":
        if player_input_row == "1":
            player_move = int(player_input_row) - 1
            return player_move
        elif player_input_row == "2":
            player_move = int(player_input_row) + 1
            return player_move
        elif player_input_row == "3":
            player_move = int(player_input_row) + 3
            return player_move
    elif player_input_col == "b":
        if player_input_row == "1":
            player_move = int(player_input_row)
            return player_move
        elif player_input_row == "2":
            player_move = int(player_input_row) + 2
            return player_move
        elif player_input_row == "3":
            player_move = int(player_input_row) + 4
            return player_move
    elif player_input_col == "c":
        if player_input_row == "1":
            player_move = int(player_input_row) + 1
            return player_move
        elif player_input_row == "2":
            player_move = int(player_input_row) + 3
            return player_move
        elif player_input_row == "3":
            player_move = int(player_input_row) + 5
            return player_move


def check_move(board, move, turn):
    if board[move] == " ":
        if turn == 1:
            board[move] = "X"
        else:
            board[move] = "O"
        return True
    else:
        print("Invalid Move")
        return False


def check_winner(board, winner):
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for condition in win_conditions:
        total_x = 0
        total_o = 0
        for idx in condition:
            if board[idx] == "X":
                total_x += 1
                if total_x == 3:
                    winner = 1
            elif board[idx] == "O":
                total_o += 1
                if total_o == 3:
                    winner = -1
    return winner


main()

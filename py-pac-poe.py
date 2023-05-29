def main():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    turn = 1
    move_count = 0
    winner = 0
    init()
    while winner == 0:
        turn_order(winner, move_count, turn)
        player_move = get_move()
        if check_move(board, player_move, turn):
            turn *= -1
            move_count += 1
            check_winner(board, turn, move_count, winner)
            render_board(board)


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


def turn_order(winner, move_count, turn):
    player1 = "X"
    player2 = "O"
    if winner == 0 and move_count == 9:
        print(f"Sorry No One Wins - CAT Game")
    elif winner:
        print(f"Congrats! {winner} has won")
    elif turn == 1:
        print(f"It is {player1}'s turn\n")
    else:
        print(f"It is {player2}'s turn\n")


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


# go through board list, check for a1 = index 0, a2 = index1 ...
# def check_move(board, move, turn):
#     if board[move] != "X" or board[move] != "O":
#         if turn == 1:
#             board[move] = "X"
#         else:
#             board[move] = "O"
#     else:
#         print("Please enter a different move: ")


def check_winner(board, turn, move_count, winner):
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
        total = 0
        check_list = [win_conditions[condition]]
        if turn == 1:
            for idx in check_list:
                if board[idx] == "X":
                    total += 1
                if total == 3:
                    winner == 1
                    return winner


main()

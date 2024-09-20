board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner = None
game_running = True


# Print the game board
def print_board(board):
    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("----------")
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("----------")
    print("{} | {} | {}".format(board[6], board[7], board[8]))


# Take player input
def player_input(board):
    player_inp = int(input("Enter a number 1-9: "))
    if 1 <= player_inp <= 9 and board[player_inp - 1] == "-":
        board[player_inp-1] = current_player
    else:
        print("This position is taken.")


# Check for win or tie
def check_horizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[1] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = current_player
        return True


def check_diagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[1] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = current_player
        return True


def check_vertical(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] !='-'):
        winner = current_player
        return True


def check_tie(board):
    global game_running
    if "-" not in board:
        game_running = False
        print(board)
        print("It's a tie!")


def check_winner():
    global game_running
    if check_diagonal(board) or check_vertical(board) or check_horizontal(board):
        print(f"The winner is {winner}")
        game_running = False


# Switch player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Check for win or tie


# Game running
while game_running:
    print_board(board)
    player_input(board)
    check_winner()
    check_tie(board)
    switch_player()



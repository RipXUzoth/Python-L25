board = [" " for _ in range(9)]
def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()
def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True 
    return False
def is_draw():
    return " " not in board
def play_game():
    current_player = "X"
    print("Welcome to tic tack toe")
    print("PLayer X goes first, positions are 1 to 9: ")
    print_board()
    while True:
        try:
            move = int(input(f"Player {current_player}, Enter your move (1-9): ")) -1
            if board[move] == " ":
                board[move] = current_player
                print_board()
                if check_winner(current_player):
                    print(f"🥳 Player {current_player} wins!")
                    break
                elif is_draw():
                    print("Its a draw...")
                    break
                current_player = "0" if current_player == "X" else "X"
            else: 
                print("That spot is already taken. Go Again.")
        except (ValueError, IndexError):
            print("Invalid move. Enter a number from 1 to 9.")
play_game()
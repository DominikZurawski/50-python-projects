# Import
import os
import time
import random

# Define the board
board_game = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
board_instr = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]



def print_header():
    print(
        """
     _____  _  ____     _____  ____  ____     _____  ____  _____
    /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    
      / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      
      | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     
      \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\
    
    
    
    """)


# Define the print_board function
def print_board(board):
    print("     |     |     ")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "   ")
    print("     |     |     ")
    print("-----|-----|-----")
    print("     |     |     ")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + "   ")
    print("     |     |     ")
    print("-----|-----|-----")
    print("     |     |     ")
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + "   ")
    print("     |     |     ")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(0.2)


def is_winner(board, player):
    winner = False
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        clear_screen()
        print_header()
        print_board(board_game)
        print(f"{player} wins! Congratulations")
        winner = True
        return winner
    return winner


def is_board_full(board):
    return False if " " in board else True


def get_computer_move(board, player):
    # if the center square is empty choose that
    if board[5] == " ":
        return 5

    while True:
        move = random.randint(1, 9)
        # if the move is blank, go ahead and return, otherwise try again
        if board[move] == " ":
            return move
            break
    return 5


def player_move():
    choice = int(input("Please choose a number for X. "))
    time.sleep(0.3)

    # Check to see if the space is empty first
    if board_game[choice] == " ":
        board_game[choice] = "X"
    else:
        print("Sorry, that space is not empty!")
        time.sleep(0.2)
        player_move()


choice = ''
while True:
    if choice == '':
        clear_screen()
        print_header()
        print_board(board_instr)
    else:
        clear_screen()
        print_header()
        print_board(board_game)

    player_move()
    if is_winner(board_game, "X"):
        break

    clear_screen()
    print_board(board_game)

    if is_board_full(board_game):
        print("Tie!")
        break

    choice = get_computer_move(board_game, "O")

    if board_game[choice] == " ":
        board_game[choice] = "O"

    if is_winner(board_game, "O"):
        break

    if is_board_full(board_game):
        print("Tie!")
        break

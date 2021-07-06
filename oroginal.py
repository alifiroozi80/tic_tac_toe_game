from os import system
from random import choice

board_dict = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}

player = input("Play Singular or Twosome? [s/t]: ").lower()
rand_list = list(range(1, 10))


def show_board(board):
    print(board[1], "|", board[2], "|", board[3])
    print("--+---+--")
    print(board[4], "|", board[5], "|", board[6])
    print("--+---+--")
    print(board[7], "|", board[8], "|", board[9])


def x_player():
    x = int(input("X -> Where do you want to put X [1 - 9]?: "))
    if board_dict[x] == " ":
        board_dict[x] = "X"
        rand_list.remove(x)
    else:
        print(f"Place {x} is already filled in!")
        x_player()


def o_player():
    if player == "t":
        o = int(input("O -> Where do you want to put O [1 - 9]?: "))
        if board_dict[o] == " ":
            board_dict[o] = "O"
        else:
            print(f"Place {o} is already filled in!")
            o_player()
    else:
        board_dict[choice(rand_list)] = "O"


def clear_scr():
    clear()
    show_board(board_dict)


def clear():
    system('clear')


def check_for_winner():
    if (board_dict[1] == "X" and board_dict[2] == "X" and board_dict[3] == "X") or \
            (board_dict[4] == "X" and board_dict[5] == "X" and board_dict[6] == "X") or \
            (board_dict[7] == "X" and board_dict[8] == "X" and board_dict[9] == "X") or \
            (board_dict[1] == "X" and board_dict[5] == "X" and board_dict[9] == "X") or \
            (board_dict[1] == "X" and board_dict[4] == "X" and board_dict[7] == "X") or \
            (board_dict[2] == "X" and board_dict[5] == "X" and board_dict[8] == "X") or \
            (board_dict[3] == "X" and board_dict[6] == "X" and board_dict[9] == "X") or \
            (board_dict[3] == "X" and board_dict[5] == "X" and board_dict[7] == "X"):
        show_board(board_dict)
        print("\n----------- X is winner -----------")
        return True
    elif (board_dict[1] == "O" and board_dict[2] == "O" and board_dict[3] == "O") or \
            (board_dict[4] == "O" and board_dict[5] == "O" and board_dict[6] == "O") or \
            (board_dict[7] == "O" and board_dict[8] == "O" and board_dict[9] == "O") or \
            (board_dict[1] == "O" and board_dict[5] == "O" and board_dict[9] == "O") or \
            (board_dict[1] == "O" and board_dict[4] == "O" and board_dict[7] == "O") or \
            (board_dict[2] == "O" and board_dict[5] == "O" and board_dict[8] == "O") or \
            (board_dict[3] == "O" and board_dict[6] == "O" and board_dict[9] == "O") or \
            (board_dict[3] == "O" and board_dict[5] == "O" and board_dict[7] == "O"):
        show_board(board_dict)
        print("\n----------- O is winner -----------")
        return True


def check():
    if check_for_winner():
        return True
    elif i == 8:
        show_board(board_dict)
        print("\n----------- Draw! -----------")
        return True
    clear_scr()


show_board(board_dict)

i = 0
while i < 9:
    try:
        x_player()
        if check():
            break
        o_player()
        if check():
            break
    except KeyError:
        print("Enter a number between 1 to 9")
    except ValueError:
        print("That's not a number bro!")
    else:
        i += 2

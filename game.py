from os import system
from random import choice


class Game:
    def __init__(self, board, i):
        self.board = board
        self.i = i
        self.player = input("Play Singular or Twosome? [s/t]: ").lower()
        self.rand_list = list(range(1, 10))

    def show_board(self):
        print(self.board[1], "|", self.board[2], "|", self.board[3])
        print("--+---+--")
        print(self.board[4], "|", self.board[5], "|", self.board[6])
        print("--+---+--")
        print(self.board[7], "|", self.board[8], "|", self.board[9])

    def x_player(self):
        x = int(input("X -> Where do you want to put X [1 - 9]?: "))
        if self.board[x] == " ":
            self.board[x] = "X"
            self.rand_list.remove(x)
        else:
            print(f"Place {x} is already filled in!")
            self.x_player()

    def o_player(self):
        if self.player == "t":
            o = int(input("O -> Where do you want to put O [1 - 9]?: "))
            if self.board[o] == " ":
                self.board[o] = "O"
            else:
                print(f"Place {o} is already filled in!")
                self.o_player()
        else:
            self.board[choice(self.rand_list)] = "O"

    def clear(self):
        system('clear')

    def clear_scr(self):
        self.clear()
        self.show_board()

    def check_for_winner(self):
        if (self.board[1] == "X" and self.board[2] == "X" and self.board[3] == "X") or \
                (self.board[4] == "X" and self.board[5] == "X" and self.board[6] == "X") or \
                (self.board[7] == "X" and self.board[8] == "X" and self.board[9] == "X") or \
                (self.board[1] == "X" and self.board[5] == "X" and self.board[9] == "X") or \
                (self.board[1] == "X" and self.board[4] == "X" and self.board[7] == "X") or \
                (self.board[2] == "X" and self.board[5] == "X" and self.board[8] == "X") or \
                (self.board[3] == "X" and self.board[6] == "X" and self.board[9] == "X") or \
                (self.board[3] == "X" and self.board[5] == "X" and self.board[7] == "X"):
            self.show_board()
            print("\n----------- X is winner -----------")
            return True
        elif (self.board[1] == "O" and self.board[2] == "O" and self.board[3] == "O") or \
                (self.board[4] == "O" and self.board[5] == "O" and self.board[6] == "O") or \
                (self.board[7] == "O" and self.board[8] == "O" and self.board[9] == "O") or \
                (self.board[1] == "O" and self.board[5] == "O" and self.board[9] == "O") or \
                (self.board[1] == "O" and self.board[4] == "O" and self.board[7] == "O") or \
                (self.board[2] == "O" and self.board[5] == "O" and self.board[8] == "O") or \
                (self.board[3] == "O" and self.board[6] == "O" and self.board[9] == "O") or \
                (self.board[3] == "O" and self.board[5] == "O" and self.board[7] == "O"):
            self.show_board()
            print("\n----------- O is winner -----------")
            return True

    def check(self):
        if self.check_for_winner():
            return True
        elif self.i == 8:
            self.show_board()
            print("\n----------- Draw! -----------")
            return True
        self.clear_scr()

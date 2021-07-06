from game import Game

board_dict = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}

game = Game(board=board_dict, i=0)
game.show_board()

while game.i < 9:
    try:
        game.x_player()
        if game.check():
            break
        game.o_player()
        if game.check():
            break
    except KeyError:
        print("Enter a number between 1 to 9")
    except ValueError:
        print("That's not a number bro!")
    else:
        game.i += 2

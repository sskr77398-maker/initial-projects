import math
import random

class player:
    def __init__(self, letter):
        # letter is x for o
        self.letter = letter

    def get_move(self, game):
            pass

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        val_square = False
        val = None
        while not val_square:
            square = input(self.letter + '\'s turn. Input move(0-9: ')
            # condition for check the input is valid or not by trying it to cast
            # it to an integer, and if it's not we say invalid
            # if this space is not available on the board , we also say same(invalid).

            # try:
            #     val = int(square)
            #     if val not in game.available_moves()

        




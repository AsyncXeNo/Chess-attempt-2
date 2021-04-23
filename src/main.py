import sys
import os
from game import Game

sys.path.append(os.getcwd())

game = Game()

if __name__ == '__main__':
    game.run()
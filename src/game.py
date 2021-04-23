import pygame
import math
import sys

from constants import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board


class Game:
    def __init__(self):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT,))
        pygame.display.set_caption('chess')
        self.rect = self.win.get_rect()
        
        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.board = Board()

    def redraw_game_window(self):
        self.win.fill(pygame.Color('gold'))

        self.board.draw(self.win)

        pygame.display.update()
        self.clock.tick(self.FPS)

    def click(self, pos):
        x = pos[0]
        y = pos[1]

        square = ((x // SQUARE_SIZE) + 1, 8 - (y // SQUARE_SIZE))
        print(square)

        if self.board.selected_piece:
            pass

        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board.board[col][row]:
                    self.board.board[col][row].unselect()
                    self.board.selected_piece = None
        
        if self.board.board[square[0]-1][square[1]-1]:
            print('piece selected')
            self.board.selected_piece = self.board.board[square[0]-1][square[1]-1]
            self.board.board[square[0]-1][square[1]-1].select()

    def run(self):
        run = True
        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                    quit()

                if event.type == pygame.MOUSEMOTION:
                    pass

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.click(pos)

            self.redraw_game_window()
            for row in range(self.board.rows):
                for col in range(self.board.cols):
                    if self.board.board[col][row]:
                        if self.board.board[col][row].isSelected():
                            print(self.board.board[col][row])

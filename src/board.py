import pygame

from constants import SQUARE_SIZE, number_to_file
from piece import *

class Board:
    def __init__(self):
        self.rows = 8
        self.cols = 8

        self.light = (234,240,206)
        self.dark = (187,190,100)

        self.board = [[None for _ in range(self.rows)] for _ in range(self.cols)]

        self.startingFEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.fen_decrypter(self.startingFEN)

        self.selected_piece = None

        # for row in range(len(self.board)):
        #     for col in range(len(self.board[row])):
        #         print(f'[SQUARE] {number_to_file[col+1]}{row+1} [PIECE] {self.board[col][row]}')
    
    def fen_decrypter(self, fen_string):
        pieces = []

        fen_string = fen_string.split(' ')[0]

        piece_type_from_symbol = {
            'p' : Pawn,
            'k' : King,
            'n' : Knight,
            'b' : Bishop,
            'q' : Queen,
            'r' : Rook
        }

        row, col = 8, 0

        for letter in fen_string:
            if letter == '/':
                col = 0
                row -= 1
            else:
                if letter.isnumeric():
                    col += int(letter)
                else:
                    piece_color = 'w' if letter.isupper() else 'b'
                    piece = piece_type_from_symbol[letter.lower()](col+1, row, piece_color)
                
                    col += 1
                    pieces.append(piece)
        
        for piece in pieces:
            self.board[piece.col-1][piece.row-1] = piece

    def draw(self, win):
        win.fill(self.dark)
        for row in range(self.rows):
            for col in range(row % 2, self.cols, 2):
                pygame.draw.rect(win, self.light, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        self.draw_pieces(win)

    def draw_pieces(self, win):
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                if self.board[col][row]:
                    self.board[col][row].draw(win)

    def update_piece_pos(self, piece):
        pass

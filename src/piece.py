import pygame

from constants import SQUARE_SIZE, number_to_file

# importing sprites
b_bishop = pygame.image.load('assets/black/bishop.png')
b_king = pygame.image.load('assets/black/king.png')
b_queen = pygame.image.load('assets/black/queen.png')
b_knight = pygame.image.load('assets/black/knight.png')
b_rook = pygame.image.load('assets/black/rook.png')
b_pawn = pygame.image.load('assets/black/pawn.png')

w_bishop = pygame.image.load('assets/white/bishop.png')
w_king = pygame.image.load('assets/white/king.png')
w_queen = pygame.image.load('assets/white/queen.png')
w_knight = pygame.image.load('assets/white/knight.png')
w_rook = pygame.image.load('assets/white/rook.png')
w_pawn = pygame.image.load('assets/white/pawn.png')

b = [b_bishop, b_king, b_knight, b_queen, b_rook, b_pawn]
w = [w_bishop, w_king, w_knight, w_queen, w_rook, w_pawn]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (64, 64,)))

for img in w:
    W.append(pygame.transform.scale(img, (64, 64,)))
# ------------------------------------------------------------
    

class Piece:
    img = None

    def __init__(self, col, row, color):
        self.row = row
        self.col = col 
        self.pos = pygame.math.Vector2(self.col, self.row) 
        
        self.color = color
        
        self.selected = False

    def __str__(self):
        return f'{number_to_file[self.col]}{self.row}'

    def move(self):
        pass

    def select(self):
        self.selected = True
    
    def unselect(self):
        self.selected = False

    def isSelected(self):
        return self.selected

    def draw(self, screen):
        if self.color == 'w':
            imgToDraw = W[self.img]
            imgRect = imgToDraw.get_rect()
            imgRect.center = ((self.col*SQUARE_SIZE)-(SQUARE_SIZE//2), ((9-self.row)*SQUARE_SIZE)-(SQUARE_SIZE//2))
        else:
            imgToDraw = B[self.img]
            imgRect = imgToDraw.get_rect()
            imgRect.center = ((self.col*SQUARE_SIZE)-(SQUARE_SIZE//2), ((9-self.row)*SQUARE_SIZE)-(SQUARE_SIZE//2))

        screen.blit(imgToDraw, imgRect)


class Bishop(Piece):
    img = 0
    symbol = 'B'

    def __str__(self):
        return f'{self.color}{self.symbol} - {number_to_file[self.col]}{self.row}'

class King(Piece):
    img = 1
    symbol = 'K'

    def __str__(self):
        return f'{self.color}{self.symbol} - {number_to_file[self.col]}{self.row}'

class Knight(Piece):
    img = 2
    symbol = 'N'

    def __str__(self):
        return f'{self.color}{self.symbol} - {number_to_file[self.col]}{self.row}'

class Pawn(Piece):
    img = 5
    symbol = 'P'

    def __str__(self):
        return f'{self.color}{self.symbol} - {number_to_file[self.col]}{self.row}'

class Queen(Piece):
    img = 3
    symbol = 'Q'

    def __str__(self):
        return f'{self.color}{self.symbol} - {number_to_file[self.col]}{self.row}'

class Rook(Piece):
    img = 4
    symbol = 'R'

    def __str__(self):
        return f'{self.color}{self.symbol} - {number_to_file[self.col]}{self.row}'

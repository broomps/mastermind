import pygame, sys
from pygame.math import Vector2
#from boards import Toard

pygame.init()

BROWN = (111, 67, 42)
DARK_BROWN = (90, 56, 40)

cell_size = 10
number_of_cells = 50

screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))

pygame.display.set_caption("Mastermind")

clock = pygame.time.Clock()


class Board:
    def __init__(self):
        self.position = Vector2(5, 6)
    
    def draw(self):
        board_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size * 5, cell_size * 10)
        pygame.draw.rect(screen, DARK_BROWN, board_rect)


board = Board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Thank you for playing!")
    
    #Drawing
    screen.fill(BROWN)
    board.draw()

    pygame.display.update()
    clock.tick(30)
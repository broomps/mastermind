import pygame, sys
from pygame.math import Vector2
from boards import *

pygame.init()

cell_size = 10
number_of_cells = 50

screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))

pygame.display.set_caption("Mastermind")

clock = pygame.time.Clock()

board = Board(Vector2, pygame)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Thank you for playing!")
    
    #Drawing
    screen.fill(board.BROWN)
    board.draw(screen, cell_size, Vector2(4, 2))

    pygame.display.update()
    clock.tick(30)
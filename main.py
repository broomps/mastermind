import pygame, sys
from pygame.math import Vector2
from board import *
from button import *

pygame.init()

cell_size = 10
number_of_cells = 50

screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))

pygame.display.set_caption("Mastermind")

clock = pygame.time.Clock()

board = Board(Vector2, pygame)

screen.fill(board.BROWN)
board.draw(screen, cell_size, Vector2(4, 1))

button1 = Button(pygame)
button2 = Button(pygame)
button3 = Button(pygame)
button4 = Button(pygame)

button1.initial_draw(screen, cell_size, 15, 3)
button2.initial_draw(screen, cell_size, 23, 3)
button3.initial_draw(screen, cell_size, 31, 3)
button4.initial_draw(screen, cell_size, 39, 3)

while True:
    #Checks if the x to close button is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Thank you for playing!")
    
    #Checking for collisions
    button1.check_clicked(screen, cell_size, 15, 3)
    button2.check_clicked(screen, cell_size, 23, 3)
    button3.check_clicked(screen, cell_size, 31, 3)
    button4.check_clicked(screen, cell_size, 39, 3)

    #Game clock
    pygame.display.update()
    clock.tick(30)
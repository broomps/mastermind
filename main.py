import pygame, sys, random
from pygame.math import Vector2
from board import *
from button import *
from textbutton import *
from keypeg import *

buttons = [0, 0, 0, 0]
answer = []
for i in range(4):
    answer.append(random.randint(0, 5))
print(answer)

pygame.init()

cell_size = 10
number_of_cells = 50

screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))
pygame.display.set_caption("Mastermind")

font = pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 20)

clock = pygame.time.Clock()

board = Board(Vector2, pygame)

x = 7
y = 1

screen.fill(board.BROWN)
board.draw(screen, cell_size, Vector2(x, y))

button1 = Button(pygame)
button2 = Button(pygame)
button3 = Button(pygame)
button4 = Button(pygame)

button1.initial_draw(screen, cell_size, x + 11, y + 2)
button2.initial_draw(screen, cell_size, x + 19, y + 2)
button3.initial_draw(screen, cell_size, x + 27, y + 2)
button4.initial_draw(screen, cell_size, x + 35, y + 2)

guess_button = Text_Button(pygame, "Guess")
guess_button.draw(screen, cell_size, 0, 0, font)

won = False
count = 0

while True:
    #Checks if the x to close button is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Thank you for playing!")
    
    #Checking for collisions
    buttons[0] = button1.check_clicked(screen, cell_size, x + 11, y + 2)
    buttons[1] = button2.check_clicked(screen, cell_size, x + 19, y + 2)
    buttons[2] = button3.check_clicked(screen, cell_size, x + 27, y + 2)
    buttons[3] = button4.check_clicked(screen, cell_size, x + 35, y + 2)

    guessed = guess_button.check_click(screen, cell_size, 0, 0)
    if guessed == True:
        correct = guess_button.check_correct(answer, buttons)
        peg1 = Key_Peg(pygame)
        peg2 = Key_Peg(pygame)
        peg3 = Key_Peg(pygame)
        peg4 = Key_Peg(pygame)
        peg1.place(screen, cell_size, 9, y + 2, correct[0])
        peg2.place(screen, cell_size, 11, y + 2, correct[1])
        peg3.place(screen, cell_size, 9, y + 4, correct[2])
        peg4.place(screen, cell_size, 11, y + 4, correct[3])

        won = guess_button.check_win(correct)
        print(won)


    #Game clock
    pygame.display.update()
    clock.tick(60)

    if won == True:
        board.win(screen, cell_size, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 50))
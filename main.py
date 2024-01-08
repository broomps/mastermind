import pygame, sys, random, time
from pygame.math import Vector2
from board import *
from button import *
from textbutton import *
from keypeg import *

buttons = [0, 0, 0, 0]
answer = []
for i in range(4):
    answer.append(random.randint(0, 5))

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

row = 0
end = False

y_values = [(y + 2), (y + 7), (y + 12), (y + 17), (y + 22), (y + 27), (y + 32), (y + 37), (y + 42)]

while True:
    #Checks if the x to close button is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Thank you for playing!")
    
    #Checking for collisions
    buttons[0] = button1.check_clicked(screen, cell_size, x + 11, y_values[row])
    buttons[1] = button2.check_clicked(screen, cell_size, x + 19, y_values[row])
    buttons[2] = button3.check_clicked(screen, cell_size, x + 27, y_values[row])
    buttons[3] = button4.check_clicked(screen, cell_size, x + 35, y_values[row])

    guessed = guess_button.check_click(screen, cell_size, 0, 0)
    if guessed == True:
        correct = guess_button.check_correct(answer, buttons)
        peg1 = Key_Peg(pygame)
        peg2 = Key_Peg(pygame)
        peg3 = Key_Peg(pygame)
        peg4 = Key_Peg(pygame)
        peg1.place(screen, cell_size, 9, y_values[row], correct[0])
        peg2.place(screen, cell_size, 11, y_values[row], correct[1])
        peg3.place(screen, cell_size, 9, y_values[row] + 2, correct[2])
        peg4.place(screen, cell_size, 11, y_values[row] + 2, correct[3])

        won = guess_button.check_win(correct)

        if won == True:
            board.win(screen, cell_size, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 30), row + 1)
        else:
            row += 1
            try:
                button1.initial_draw(screen, cell_size, x + 11, y_values[row])
                button2.initial_draw(screen, cell_size, x + 19, y_values[row])
                button3.initial_draw(screen, cell_size, x + 27, y_values[row])
                button4.initial_draw(screen, cell_size, x + 35, y_values[row])
            except IndexError:
                board.lose(screen, cell_size, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 50))
                print(row)
                end = True

    #Game clock
    pygame.display.update()
    clock.tick(60)

    if end == True:
        time.sleep(5)
        pygame.quit()
        sys.exit("Thank you for playing!")
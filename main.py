import pygame, sys, random, time
from pygame.math import Vector2
from board import *
from button import *
from textbutton import *
from keypeg import *

#Initializes all of the variables used in the program
clicked = False
won = False
row = 0
end = False
x = 7
y = 1
cell_size = 10
number_of_cells = 50
buttons = [0, 0, 0, 0]

#Pygame initialization
pygame.init()

#Screen is set up with the mastermind caption
screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells))
pygame.display.set_caption("Mastermind")

#FPS is initialized
clock = pygame.time.Clock()

#The board instance of class Board is initialized
board = Screen(Vector2, pygame)

#Start button initialization
start_button = Text_Button(pygame, "START")

#Intantiates all of the code pegs
button1 = Button(pygame)
button2 = Button(pygame)
button3 = Button(pygame)
button4 = Button(pygame)

#All text buttons are instantiated
guess_button = Text_Button(pygame, "Guess")

quit_button = Text_Button(pygame, "Quit")

save_button = Text_Button(pygame, "Save")

restore_button = Text_Button(pygame, "Restore")

#Wipes the save file
with open("save.txt", "w") as f:
    pass
#Fill the background
screen.fill(board.BROWN)

def draw():

    #Draws the initial board
    board.draw(screen, cell_size, Vector2(x, y))

    #All code pegs are drawn
    button1.initial_draw(screen, cell_size, x + 11, y + 2)
    button2.initial_draw(screen, cell_size, x + 19, y + 2)
    button3.initial_draw(screen, cell_size, x + 27, y + 2)
    button4.initial_draw(screen, cell_size, x + 35, y + 2)

    #ALl text buttons are drawn
    guess_button.draw(screen, cell_size, 0, 0, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 20), 6, 2)
    quit_button.draw(screen, cell_size, 0, 4, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 20), 4.5, 2)
    save_button.draw(screen, cell_size, 0, 8, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 20), 4.5, 2)

def guess(row):
    #Creates a list with all all the values for if they are correct
    correct = guess_button.check_correct(answer, buttons)
    #Initializes all of the key pegs
    peg1 = Key_Peg(pygame)
    peg2 = Key_Peg(pygame)
    peg3 = Key_Peg(pygame)
    peg4 = Key_Peg(pygame)
    #Places all of the key pegs with the correct colour
    peg1.place(screen, cell_size, 9, y_values[row], correct[0])
    peg2.place(screen, cell_size, 11, y_values[row], correct[1])
    peg3.place(screen, cell_size, 9, y_values[row] + 2, correct[2])
    peg4.place(screen, cell_size, 11, y_values[row] + 2, correct[3])

    #Autosave
    with open("save.txt", "a") as f:
        button = ""
        corrects = ""
        for i in buttons:
            button += str(i)
        
        for i in correct:
            for j in i:
                j = str(j)
                if j == "False":
                    corrects += "0"
                elif j == "True":
                    corrects += "1"
        button += corrects
        f.write(button)
    #Checks if they have won
    won = guess_button.check_win(correct)

    #If they have won
    if won == True:
        #The winning screen is displayed
        board.win(screen, cell_size, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 30), row + 1)
    else:
        #Row + 1 means go to the next row down
        row += 1
        try:
            #Try to draw another row of buttons
            button1.initial_draw(screen, cell_size, x + 11, y_values[row])
            button2.initial_draw(screen, cell_size, x + 19, y_values[row])
            button3.initial_draw(screen, cell_size, x + 27, y_values[row])
            button4.initial_draw(screen, cell_size, x + 35, y_values[row])
        except IndexError:
            #If they have made the maximum number of guesses they lose
            board.lose(screen, cell_size, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 50))
            end = True
    return(row)
#Y values for the pegs is set up
y_values = [(y + 2), (y + 7), (y + 12), (y + 17), (y + 22), (y + 27), (y + 32), (y + 37), (y + 42)]

#Game loop
while True:
    #Menu loop
    while clicked != True:
        #Checks if the x to close button is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit("Thank you for playing!")
        drawn = False
        screen.fill(board.BROWN)
        start_button.draw(screen, cell_size, 10, 10, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 50), 15, 5)
        restore_button.draw(screen, cell_size, 10, 20, pygame.font.Font('retro-grade-2-font/RetroGradeItalic-2OZYv.otf', 50), 21, 6)
        
        clicked = start_button.check_click(screen, cell_size, 10, 10, 15, 5)
        if restore_button.check_click(screen, cell_size, 10, 20, 21, 6):
            row = 0
            drawn = True
            clicked = True
            with open("save.txt", "r") as f:
                savefile = f.readlines()
                for i in range(int(len(savefile[0])/16)):
                    if i == 0:
                        button1.colour = int(savefile[0][0])
                        button2.colour = int(savefile[0][1])
                        button3.colour = int(savefile[0][2])
                        button4.colour = int(savefile[0][3])
                        draw()
                        row = guess(row)

                        # #Initializes all of the key pegs
                        # peg1 = Key_Peg(pygame)
                        # peg2 = Key_Peg(pygame)
                        # peg3 = Key_Peg(pygame)
                        # peg4 = Key_Peg(pygame)

                        # correct_list = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                        # for i in range(4):
                        #     for j in range(3):
                        #         correct_list[i][j] = savefile[0][((i*3) + j) + 4]
                        # print(correct_list)
                        # #Places all of the key pegs with the correct colour
                        # peg1.place(screen, cell_size, 9, y_values[row], correct_list[0])
                        # peg2.place(screen, cell_size, 11, y_values[row], correct_list[1])
                        # peg3.place(screen, cell_size, 9, y_values[row] + 2, correct_list[2])
                        # peg4.place(screen, cell_size, 11, y_values[row] + 2, correct_list[3])
                    else:
                        button1.colour = int(savefile[0][0 + (4*i)])
                        button2.colour = int(savefile[0][1 + (4*i)])
                        button3.colour = int(savefile[0][2 + (4*i)])
                        button4.colour = int(savefile[0][3 + (4*i)])

                        row = guess(row)
                        #Try to draw another row of buttons
                        button1.initial_draw(screen, cell_size, x + 11, y_values[row])
                        button2.initial_draw(screen, cell_size, x + 19, y_values[row])
                        button3.initial_draw(screen, cell_size, x + 27, y_values[row])
                        button4.initial_draw(screen, cell_size, x + 35, y_values[row])
            #Wipes the save file
            with open("save.txt", "w") as f:
                pass


        #Game clock
        pygame.display.update()
        clock.tick(60)
    if not(drawn):
        button1.colour = 0
        button2.colour = 0
        button3.colour = 0
        button4.colour = 0
        answer = []
        #The answer is randomly generated
        for i in range(4):
            answer.append(random.randint(0, 5))
        draw()
        drawn = True
        row = 0
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

    clicked = not(save_button.check_click(screen, cell_size, 0, 8, 4.5, 2))
    if clicked == False:
        #Save
        with open("save.txt", "a") as f:
            button = ""
            for i in buttons:
                button += str(i)
            f.write(button)
    #Checks if the guess button has been clicked
    guessed = guess_button.check_click(screen, cell_size, 0, 0, 6, 2)
    if guessed == True:
        row = guess(row)
    if clicked != False:
        clicked = not(quit_button.check_click(screen, cell_size, 0, 4, 4.5, 2))

    #Game clock
    pygame.display.update()
    clock.tick(60)

    #If they have lost the game waits 5 seconds then closes
    if end == True:
        time.sleep(5)
        pygame.quit()
        sys.exit("Thank you for playing!")
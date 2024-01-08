class Text_Button:
    #Initializes all of the variables
    def __init__(self, pygame, text, darkest_brown=(62, 43, 35),dark_brown=(90, 56, 40)):
        self.pygame = pygame
        self.darkest_brown = darkest_brown
        self.dark_brown = dark_brown
        self.text = text
        self.clicked = False
    
    def draw(self, screen, cell_size, x, y, font):
        #Draws the background that the text sits on
        button_rect = self.pygame.Rect(x * cell_size, y * cell_size, cell_size * 6, cell_size * 2)
        self.pygame.draw.rect(screen, self.dark_brown, button_rect)

        #Renders the text with the font and overlays it onto the background
        text_img = font.render(self.text, True, self.darkest_brown)
        screen.blit(text_img, (x * cell_size, y * cell_size))
    
    def check_click(self, screen, cell_size, x, y):
        #get mouse position
        pos = self.pygame.mouse.get_pos()
        #Creates the button rectangle
        button_rect = self.pygame.Rect(x * cell_size, y * cell_size, cell_size * 6, cell_size * 2)

        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if self.pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return(True)
        
        #If not currently clicking another click will be allowed
        if self.pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
    
    def check_correct(self, correct_answer, buttons):
        correct=[[False, False, False], [False, False, False], [False, False, False], [False, False, False]]
        #Iterates through each button
        for i in range(4):
            #If the guess is exactly correct the right value is set to true accordingly
            if buttons[i] == correct_answer[i]:
                correct[i][0] = True
            #Iterates through the answer list
            for j in range(4):
                #Right colour wrong place the right value is set to true
                if (buttons[i] == correct_answer[j]) and (i != j):
                    correct[i][1] = True
            #If it is not correct at all then it is set accordingly
            if (correct[i][0] == False) and (correct[i][1] == False):
                correct[i][2] = True
        #It returns the ammended list of correct values
        return(correct)
    
    def check_win(self, correct, total=0):
        #Iterates through the correct list and checks how many are correct
        for i in range(len(correct)):
            if correct[i][0]:
                total += 1
        
        #If 4 are correct they win and if not the game continues
        if total == 4:
            return(True)
        else:
            return(False)
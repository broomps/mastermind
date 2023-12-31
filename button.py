class Button:
    #Initializing all of the variables aswell as pygame
    def __init__(self, pygame):
        self.colours = ((112, 214, 255), (255, 112, 166), (255, 151, 112), (255, 214, 112), (43, 237, 112), (0, 107, 166))
        self.pygame = pygame
        self.colour = 0
        self.clicked = False

    #It draws all of the buttons with green as their starting colour
    def initial_draw(self, screen, cell_size, x, y):
        button_rect = self.pygame.Rect(x * cell_size, y * cell_size, cell_size * 4, cell_size * 4)
        self.pygame.draw.rect(screen, self.colours[self.colour%len(self.colours)], button_rect)

    def check_clicked(self, screen, cell_size, x, y):
        #get mouse position
        pos = self.pygame.mouse.get_pos()
        #Creates the button rectangle
        button_rect = self.pygame.Rect(x * cell_size, y * cell_size, cell_size * 4, cell_size * 4)

        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if self.pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                #It iterates through the colours each time the button is clicked and returns what colour it is on
                self.colour += 1
                self.pygame.draw.rect(screen, self.colours[self.colour%len(self.colours)], button_rect)
        
        #If not currently clicking another click will be allowed
        if self.pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return(self.colour%len(self.colours))
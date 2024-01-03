class Button:
    def __init__(self, pygame, white=(255,255,255), black=(0,0,0), green =(152,229,165), red=(172,56,52), orange=(252,138,23), blue = (43,98,244), yellow=(249,224,118), brown=(154,123,79)):
        self.colours = (white, black, green, red, orange, blue, yellow , brown)
        self.pygame = pygame
        self.colour = 0
        self.clicked = False

    def initial_draw(self, screen, cell_size, x, y):
        button_rect = self.pygame.Rect(x * cell_size, y * cell_size, cell_size * 4, cell_size * 4)
        self.pygame.draw.rect(screen, self.colours[self.colour], button_rect)


    def check_clicked(self, screen, cell_size, x, y):
        #get mouse position
        pos = self.pygame.mouse.get_pos()
        #Creates the button rectangle
        button_rect = self.pygame.Rect(x * cell_size, y * cell_size, cell_size * 4, cell_size * 4)

        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if self.pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.colour += 1
                self.pygame.draw.rect(screen, self.colours[self.colour%len(self.colours)], button_rect)
        
        if self.pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
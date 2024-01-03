class Text_Button:
    def __init__(self, pygame, text, darkest_brown=(62, 43, 35),dark_brown=(90, 56, 40)):
        self.pygame = pygame
        self.darkest_brown = darkest_brown
        self.dark_brown = dark_brown
        self.text = text
        self.clicked = False
    
    def draw(self, screen, cell_size, x, y, font):
        button_rect = self.pygame.Rect(x * cell_size, y * cell_size, cell_size * 6, cell_size * 2)
        self.pygame.draw.rect(screen, self.dark_brown, button_rect)

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
        
        #If not currently clicking another click will be allowed
        if self.pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
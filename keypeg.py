class Key_Peg:
    #All of the colours are initialized
    def __init__(self, pygame, green=(0, 179, 138), amber=(242, 172, 66), red=(234, 50, 74)):
        self.green = green
        self.amber = amber
        self.red = red
        self.pygame = pygame
    
    def place(self, screen, cell_size, x, y, correct):
        #Creates a rectangle for the peg
        peg_rect = self.pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)

        #It checks if it is correct and chooses the correct colour accordingly
        if correct[0]:
            self.pygame.draw.rect(screen, self.green, peg_rect)
        elif correct[1]:
            self.pygame.draw.rect(screen, self.amber, peg_rect)
        else:
            self.pygame.draw.rect(screen, self.red, peg_rect)
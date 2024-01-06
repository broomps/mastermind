class Key_Peg:
    #All of the colours are initialized
    def __init__(self, pygame, green=(0, 179, 138), amber=(242, 172, 66), red=(234, 50, 74)):
        self.green = green
        self.amber = amber
        self.red = red
        self.pygame = pygame
    
    def place(self, screen, cell_size, x, y, correct):
        #It checks if it is correct and chooses the correct colour accordingly
        if correct[0]:
            self.pygame.draw.circle(screen, self.green, (x * cell_size, y * cell_size), 0.5*cell_size)
        elif correct[1]:
            self.pygame.draw.circle(screen, self.amber, (x * cell_size, y * cell_size), 0.5*cell_size)
        else:
            self.pygame.draw.circle(screen, self.red, (x * cell_size, y * cell_size), 0.5*cell_size)
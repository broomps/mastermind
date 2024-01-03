class Board:
    #Initializing all of the variables
    def __init__(self, Vector2, pygame, brown=(111, 67, 42),dark_brown=(90, 56, 40), darkest_brown=(62, 43, 35)):
        self.Vector2 = Vector2
        self.pygame = pygame
        self.BROWN = brown
        self.DARK_BROWN = dark_brown
        self.DARKEST_BROWN = darkest_brown
    
    def draw(self, screen, cell_size, position):
        #Draws the basic brown board as a rectangle
        board_rect = self.pygame.Rect(position.x * cell_size, position.y * cell_size, cell_size * 42, cell_size * 48)
        self.pygame.draw.rect(screen, self.DARK_BROWN, board_rect)

        #Draws a dark line to seperate the key pegs and the code pegs
        line_rect = self.pygame.Rect((position.x + 7) * cell_size, position.y * cell_size, cell_size, cell_size * 48)
        self.pygame.draw.rect(screen, self.DARKEST_BROWN, line_rect)
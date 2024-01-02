class Board:
    def __init__(self, Vector2, pygame, brown=(111, 67, 42),dark_brown=(90, 56, 40), darkest_brown=(62, 43, 35)):
        self.Vector2 = Vector2
        self.pygame = pygame
        self.BROWN = brown
        self.DARK_BROWN = dark_brown
        self.DARKEST_BROWN = darkest_brown
#        self.position = Vector2(5, 4)
    
    def draw(self, screen, cell_size, position):
        board_rect = self.pygame.Rect(position.x * cell_size, position.y * cell_size, cell_size * 42, cell_size * 46)
        self.pygame.draw.rect(screen, self.DARK_BROWN, board_rect)

        line_rect = self.pygame.Rect((position.x + 7) * cell_size, position.y * cell_size, cell_size, cell_size * 46)
        self.pygame.draw.rect(screen, self.DARKEST_BROWN, line_rect)
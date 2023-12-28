class Toard:
    def __init__(self, Vector2, pygame):
        self.Vector2 = Vector2
        self.pygame = pygame
        self.position = Vector2(5, 6)
    
    def draw(self, screen, cell_size, DARK_BROWN):
        board_rect = self.pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size * 5, cell_size * 10)
        self.pygame.draw.rect(screen, DARK_BROWN, board_rect)
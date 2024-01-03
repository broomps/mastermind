class Button:
    def __init__(self, pygame, white=(255,255,255), black=(0,0,0), green =(152,229,165), red=(172,56,52), orange=(252,138,23), blue = (43,98,244), yellow=(249,224,118), brown=(154,123,79)):
        self.white = white
        self.black = black
        self.green = green
        self.red = red
        self.orange = orange
        self.blue = blue
        self.yellow = yellow
        self.brown = brown
        self.pygame = pygame

    def draw(self, screen, cell_size, x, y):
        button1_rect = self.pygame.Rect(x * cell_size, y * cell_size, cell_size * 4, cell_size * 4)
        self.pygame.draw.rect(screen, self.green, button1_rect)
import pygame, sys

pygame.init()

BROWN = (111, 67, 42)
DARK_BROWN = (90, 56, 40)

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Mastermind")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit("Thank you for playing!")
    
    screen.fill(BROWN)
    pygame.display.update()
    clock.tick(30)
import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lep's World")

character_x = 50
character_y = 50

character_width = 50
character_height = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        character_x -= 5
    if keys[pygame.K_RIGHT]:
        character_x += 5
    if keys[pygame.K_UP]:
        character_y -= 5
    if keys[pygame.K_DOWN]:
        character_y += 5

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (character_x, character_y, character_width, character_height))
    pygame.display.update()


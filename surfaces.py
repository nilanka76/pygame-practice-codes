import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)

# test_surface = pygame.Surface((100,200))
# test_surface.fill((255,0,0))

background_surface = pygame.image.load('images/background.jpg')
character_surface = pygame.image.load('images/character.png')
text_surface = text_font.render('Toradora', True, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(background_surface, (0,0))
    screen.blit(character_surface, (-300,-100))
    screen.blit(text_surface, (0,300))

    pygame.display.update()
    clock.tick(60)
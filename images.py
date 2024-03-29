import pygame
def renderplayer():
    player = pygame.image.load("Graphics/player.png").convert_alpha()
    player = pygame.transform.scale(player, (50,50))
    return player

def renderbullet():
    bullet = pygame.image.load("Graphics/player.png").convert_alpha()
    bullet = pygame.transform.scale(bullet, (20, 20))
    return bullet
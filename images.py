import pygame
def renderplayer():
    player = pygame.image.load("Graphics/player.png").convert_alpha()
    player = pygame.transform.scale(player, (35,35))
    return player

def renderbullets():


    bullet = pygame.image.load("Graphics/ice.png").convert_alpha()
    bullet = pygame.transform.scale(bullet, (16,16))

    bomb = pygame.image.load("Graphics/coldbomb.png").convert_alpha()
    bomb = pygame.transform.scale(bomb, (50,15))
    return (bullet, bomb)


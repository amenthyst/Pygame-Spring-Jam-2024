import pygame

def renderbackground():
    coldbg = pygame.image.load("Pygame-Spring-Jam-2024/Graphics/coldbackground.jpg").convert_alpha()
    coldbg = pygame.transform.scale(coldbg, (1000,600))
    return coldbg
def renderplayer():
    player = pygame.image.load("Pygame-Spring-Jam-2024/Graphics/player.png").convert_alpha()
    player = pygame.transform.scale(player, (35,35))
    return player

def renderbullets():


    bullet = pygame.image.load("Pygame-Spring-Jam-2024/Graphics/ice.png").convert_alpha()
    bullet = pygame.transform.scale(bullet, (16,16))

    bomb = pygame.image.load("Pygame-Spring-Jam-2024/Graphics/coldbomb.png").convert_alpha()
    bomb = pygame.transform.scale(bomb, (50,15))
    return (bullet, bomb)


import pygame
def renderplayer():
    player = pygame.image.load("Pygame-Spring-Jam-2024/Graphics/player.png").convert_alpha()
    player = pygame.transform.scale(player, (35,35))
    return player

def renderbullet():
    bullet = pygame.image.load("Pygame-Spring-Jam-2024/Graphics/ice.png").convert_alpha()
    bullet = pygame.transform.scale(bullet, (10, 10))
    return bullet
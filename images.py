import pygame
def renderplayer():
    player = pygame.image.load("Pygame-Spring-Jam-2024/Graphics/player.png").convert_alpha()
    player = pygame.transform.scale(player, (50,50))
    return player

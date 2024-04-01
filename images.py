import pygame

def renderbackground():
    bg = pygame.image.load("Graphics/background.png").convert_alpha()
    bg = pygame.transform.scale(bg, (1000,1200))
    return bg
def renderplayer():
    player = pygame.image.load("Graphics/player.png").convert_alpha()
    player = pygame.transform.scale(player, (35,35))
    return player

def renderbullets():


    ice = pygame.image.load("Graphics/ice.png").convert_alpha()
    fire = pygame.image.load("Graphics/fire.png").convert_alpha()

    bomb = pygame.image.load("Graphics/coldbomb.png").convert_alpha()
    bomb = pygame.transform.scale(bomb, (50,15))
    return (ice, fire, bomb)


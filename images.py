import pygame

def renderbackground():
    bg = pygame.image.load("Graphics/background.png").convert_alpha()
    bg = pygame.transform.rotate(bg, 180)
    return bg
def renderplayer():
    fireplayer = pygame.image.load("Graphics/firesprite.png").convert_alpha()
    fireplayer = pygame.transform.scale(fireplayer, (75,75))
    iceplayer = pygame.image.load("Graphics/icesprite.png").convert_alpha()
    iceplayer = pygame.transform.scale(iceplayer, (75,75))
    return (fireplayer, iceplayer)
  

def renderbullets():
    ice = pygame.image.load("Graphics/ice.png").convert_alpha()
    fire = pygame.image.load("Graphics/fire.png").convert_alpha()

    icebomb = pygame.image.load("Graphics/coldbomb.png").convert_alpha()
    icebomb = pygame.transform.scale(icebomb, (50,15))

    firebomb = pygame.image.load("Graphics/firebomb.png").convert_alpha()
    firebomb = pygame.transform.scale(firebomb, (50,15))

    return (ice, fire, icebomb, firebomb)

def renderenemies():

    firebasher = pygame.image.load("Graphics/enemysprites/firebasher.png").convert_alpha()

    return (firebasher)

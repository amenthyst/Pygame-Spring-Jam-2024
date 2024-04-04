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

    icebasher = pygame.image.load("Graphics/enemysprites/icebasher.png").convert_alpha()

    coldbullet = pygame.image.load("Graphics/enemysprites/coldenemybullet.png").convert_alpha()
    coldbullet = pygame.transform.scale(coldbullet, (30, 10))

    firebullet = pygame.image.load("Graphics/enemysprites/firebasher.png").convert_alpha()
    firebullet = pygame.transform.scale(firebullet, (30, 10))

    fireshooter = pygame.image.load("Graphics/enemysprites/fireshooter.png").convert_alpha()


    iceshooter = pygame.image.load("Graphics/enemysprites/iceshooter.png").convert_alpha()

    iceshooter = pygame.transform.scale(iceshooter, (50,35))
    return (firebasher, icebasher, coldbullet, firebullet, fireshooter, iceshooter)

def rendermenuui():
    play = pygame.image.load("UI/Sprites/play_button.png").convert_alpha()
    play = pygame.transform.scale(play, (128, 64))
    return (play)


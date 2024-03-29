import pygame
from sys import exit

import Objects.bullet
import images
from Objects.player import Player

pygame.init()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Pygame-Spring-Jam-2024 Jam")
clock = pygame.time.Clock()

playersurf = images.renderplayer()

bulletgrp = pygame.sprite.Group()

playergrp = pygame.sprite.GroupSingle(Player(playersurf, (500,500), 1.4, Objects.bullet.Bullet, bulletgrp))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("white")


    playergrp.update()
    playergrp.draw(screen)

    bulletgrp.update()
    bulletgrp.draw(screen)

    pygame.display.update()
    dt = clock.tick(60)



pygame.quit()
exit()
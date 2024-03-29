import pygame
from sys import exit
import images
from Objects.player import Player

pygame.init()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Game Jam")
clock = pygame.time.Clock()

playersurf = images.renderplayer()


playergrp = pygame.sprite.GroupSingle(Player(playersurf, (500,500), 1))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("white")


    playergrp.draw(screen)
    playergrp.update()



    pygame.display.update()
    dt = clock.tick(60)



pygame.quit()
exit()
import pygame
from sys import exit
import Objects.bomb
import Objects.bullet
import Objects.particle
from Enemies.sampleenemy import Enemy
import images
from Objects.player import Player
import Systems.input

pygame.init()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Game Jam")
clock = pygame.time.Clock()

playersurf = images.renderplayer()

bulletgrp = pygame.sprite.Group()

enemygrp = pygame.sprite.Group(Enemy((600,300)))

playergrp = pygame.sprite.GroupSingle(Player(playersurf, (500,500), 1.4, Objects.bullet.Bullet, Objects.bomb.Bomb, Objects.particle.Particle, bulletgrp, enemygrp))



run = True

while run:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    Systems.input.update()

    screen.fill("white")

    playergrp.update(dt)

    playergrp.draw(screen)

    bulletgrp.update(dt)

    bulletgrp.draw(screen)

    enemygrp.draw(screen)

    enemygrp.update(dt)

    pygame.display.update()




pygame.quit()
exit()
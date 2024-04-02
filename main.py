import pygame
from sys import exit
import Objects.bomb
import Objects.bullet
import Objects.particle
from Enemies.sampleenemy import Enemy
import images
from Objects.player import Player
import Systems.input
from UI.switchbar import Switchbar
from UI.background import Background

pygame.init()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Game Jam")
clock = pygame.time.Clock()

playertuple = images.renderplayer()

MENU_MODE = 0
GAME_MODE = 1

current_mode = 0

bulletgrp = pygame.sprite.Group()

enemygrp = pygame.sprite.Group(Enemy((600,300)))

playergrp = pygame.sprite.GroupSingle(Player(playertuple,(500,500), 1.4, Objects.bullet.Bullet, Objects.bomb.Bomb, Objects.particle.Particle, bulletgrp, enemygrp))

uigrp = pygame.sprite.Group(Background(playergrp.sprites()[0]), Switchbar(playergrp.sprites()[0], (700,50), 5))

run = True

def run_menu():
    pass

def run_game():

    for obj in uigrp.sprites():
        obj.draw(screen)



    bulletgrp.draw(screen)

    enemygrp.draw(screen)

    enemygrp.update(dt)

    uigrp.update(dt)

    bulletgrp.update(dt)

    playergrp.update(dt)

    for obj in playergrp.sprites():
        obj.draw(screen)


while run:
    Systems.input.update()

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if current_mode == MENU_MODE:
        run_menu()

    elif current_mode == GAME_MODE:
        run_game()

    pygame.display.update()




pygame.quit()
exit()
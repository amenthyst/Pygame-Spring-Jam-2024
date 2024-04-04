import pygame
from sys import exit
import Objects.bomb
import Objects.bullet
import Objects.particle
import images
from Objects.player import Player
import Systems.input
from UI.switchbar import Switchbar
from UI.background import Background

from UI.wavecounter import Wavecounter

from UI.button import Button


pygame.init()

screen = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("Game Jam")
clock = pygame.time.Clock()

playertuple = images.renderplayer()

MENU_MODE = 0
GAME_MODE = 1

current_mode = 0



bulletgrp = pygame.sprite.Group()


enemygrp = pygame.sprite.Group()

playergrp = pygame.sprite.GroupSingle(Player(playertuple,(500,500), 1.4, Objects.bullet.Bullet, Objects.bomb.Bomb, Objects.particle.Particle, bulletgrp, enemygrp, 100))

ship = playergrp.sprites()[0]

uigrp = pygame.sprite.Group(Background(),Switchbar((700,50), 5),Wavecounter(enemygrp, 5, bulletgrp))




def play_game():
    global current_mode
    current_mode = GAME_MODE

menugrp = pygame.sprite.Group(Button((1000//2, 600//2), images.rendermenuui(), play_game))


run = True



def run_menu():
    menugrp.update()
    menugrp.draw(screen)

def run_game():

    for obj in uigrp.sprites():
        obj.draw(screen)



    bulletgrp.draw(screen)

    for obj in enemygrp.sprites():
        obj.draw(screen)

    enemygrp.update(dt)

    uigrp.update(dt)

    bulletgrp.update(dt)

    playergrp.update(dt)

    for obj in playergrp.sprites():
        obj.draw(screen, dt)


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
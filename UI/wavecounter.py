import pygame
from Enemies.spawnenemies import spawnenemies
from Objects.player import Player

class Wavecounter(pygame.sprite.Sprite):
    Instance = None
    def __init__(self, enemygrp: pygame.sprite.Group, maxwaves, bulletgrp):
        super().__init__()
        # wavecounter singleton
        if Wavecounter.Instance != None:
            raise Exception("Multiple wave counters, something went wrong")
        Wavecounter.Instance = self
        self.enemygrp = enemygrp
        self.currentwave = 0
        self.maxwaves = maxwaves
        self.wavetimer = 0
        self.bulletgrp = bulletgrp

    def checkwaves(self, dt):
        if len(self.enemygrp.sprites()) != 0:
            return
        self.wavetimer += dt
        if self.wavetimer < 1.5:
            return
        self.wavetimer = 0
        self.currentwave += 1
        spawnenemies(self.enemygrp, self.currentwave*3+2, self.bulletgrp)
        Player.Instance.health = 100

    def draw(self, screen):
        font = pygame.font.Font("Graphics/font.otf", 50)
        pygame.draw.rect(screen, "black", (355,20, 300,100),4)
        text = font.render(f"WAVE{self.currentwave}", False, "black")
        screen.blit(text, (370, 40))

    def update(self,dt):
        self.checkwaves(dt)


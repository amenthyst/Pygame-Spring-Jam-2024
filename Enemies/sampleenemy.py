from Objects import tags
import pygame
import images
from Objects.player import Player
from Objects.particle import Particle
import math
# base class for enemies
class Enemy(pygame.sprite.Sprite, tags.Damageable):

    def __init__(self, pos, health, dmg, speed, state, size, bulletgrp):

        super().__init__()
        self.pos = pos
        self.maxhealth = health
        self.health = health
        self.dmg = dmg
        self.speed = speed
        self.size = size
        self.state = state
        self.bulletgrp = bulletgrp
        self.image = pygame.transform.scale(images.renderbullets()[0], self.size)
        self.rect = self.image.get_rect(center=self.pos)
        self.confuseduration = 0
        self.confusetimer = 0

        self.confusion = False

        self.originalpos = pygame.math.Vector2(0, 0)

    def damage(self, amount):
        hitlist = pygame.sprite.spritecollide(self, self.bulletgrp, False)
        for obj in hitlist:
            if self.comparison(obj):
                self.health -= amount * 2
            else:
                self.health -= amount
        if self.health <= 0:
            self.kill()
        Player.Instance.addtotaldamage(amount)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.healthbar(screen)

    def healthbar(self, screen):
        pygame.draw.rect(screen, "black", (self.rect.x-3, self.rect.y-15, self.size[0] ,10), 2)
        ratio = self.health/self.maxhealth
        pygame.draw.rect(screen, "green", (self.rect.x-1, self.rect.y-13, self.size[0]*ratio-4, 6))

    def attack(self):
        pass

    def update(self,dt):
        pass

    def comparison(self, obj) -> bool:
        return (obj.state == "hot" and self.state == "cold") or (obj.state == "cold" and self.state == "hot")

    def confuse(self, dt):
        hitlist = pygame.sprite.spritecollide(self, self.bulletgrp, False)
        for obj in hitlist:
            if not isinstance(obj, Particle):
                continue
            if obj.state == "steam":
                self.confusion = True
                self.confuseduration += 0.1 if self.confuseduration < 5 else 0 # cap to the duration

        if self.confusion:
            self.confusetimer += dt
            if self.confusetimer > self.confuseduration:
                self.confusetimer = 0
                self.confusion = False

    def getangle(self, direction):
        return math.degrees(math.atan2(direction.x, direction.y)) - 90

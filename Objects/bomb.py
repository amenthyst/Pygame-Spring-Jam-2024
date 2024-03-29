import pygame
import images
import math
from Objects import tags
from Objects.particle import Particle

class Bomb(pygame.sprite.Sprite):
    def __init__(self, position, velocity, bulletgrp, enemygrp):
        super().__init__()
        self.velocity = pygame.math.Vector2(velocity)
        self.image = pygame.transform.rotate(images.renderbullets()[1], self.getangle()+90)
        self.rect = self.image.get_rect(center=position)
        self.damage = 1
        self.bulletgrp = bulletgrp
        self.enemygrp = enemygrp
    def update(self, dt):
        self.move()
        self.attack()

    def move(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
    def on_collide(self, other):
        if not isinstance(other, tags.Damageable):
            return
        other.damage(self.damage)
        for _ in range(1,500):
            self.bulletgrp.add(Particle("cold", self.bulletgrp, self.rect.center))
        self.kill()

    def attack(self):
        hitlist = pygame.sprite.spritecollide(self, self.enemygrp, False)
        for enemy in hitlist:
            self.on_collide(enemy)

    def getangle(self):
        return math.degrees(math.atan2(self.velocity.x, self.velocity.y))
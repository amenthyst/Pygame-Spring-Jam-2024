import pygame
import images
from Objects import tags

import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, velocity, enemygrp: pygame.sprite.Group, state):
        super().__init__()

        self.velocity = pygame.math.Vector2(velocity)
        self.enemygrp = enemygrp
        self.damage = 1
        self.state = state
        if self.state == "hot":
            self.image = images.renderbullets()[1]
        elif self.state == "cold":
            self.image = images.renderbullets()[0]
        self.rect = self.image.get_rect(center=tuple(position))
    def update(self, dt):
        self.attack()
        self.move()


    def move(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
    def on_collide(self, other):
        if not isinstance(other, tags.Damageable):
            return
        other.damage(self.damage)

        self.kill()

    def attack(self):
        hitlist = pygame.sprite.spritecollide(self, self.enemygrp, False)
        for obj in hitlist:
            self.on_collide(obj)


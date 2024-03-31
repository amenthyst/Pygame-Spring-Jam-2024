import pygame
import images
from Objects import tags

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, velocity, enemygrp: pygame.sprite.Group):
        super().__init__()
        self.image = pygame.transform.scale(images.renderbullets()[0], (10,10))
        self.rect = self.image.get_rect(center=tuple(position))
        self.velocity = pygame.math.Vector2(velocity)
        self.enemygrp = enemygrp
        self.damage = 1
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

import pygame
import images
from Objects import tags

import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        self.image = images.renderbullets()[0]
        self.rect = self.image.get_rect(center=tuple(position))
        self.velocity = pygame.math.Vector2(velocity)
        self.damage = 1
    def update(self, dt):
        self.move()

    def move(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
    def on_collide(self, other):
        if not isinstance(other, tags.Damageable):
            return
        other.damage(self.damage)


import pygame
import images
from tags import Damageable

import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, angle, mousevec, image, speed):
        super().__init__()
        self.position = pygame.math.Vector2(position)
        self.mousevec = pygame.math.Vector2(pygame.mouse.get_pos())
        self.direction = self.mousevec - self.position
        self.image = pygame.transform.rotate(image, self.getangle())
        self.rect = self.image.get_rect(center=position)
        self.speed = speed

    def getangle(self):
        return math.degrees(math.atan2(self.direction.x, self.direction.y))

    def move(self):
        self.direction = self.direction.normalize() * self.speed
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def update(self):
        self.move()


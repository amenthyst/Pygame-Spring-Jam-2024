import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, angle, mousevec):
        super().__init__()
        self.position = pygame.math.Vector2(position)
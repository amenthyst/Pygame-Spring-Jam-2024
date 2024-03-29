import pygame
import images

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        self.image = images.renderbullet()
        self.rect = self.image.get_rect(center=position)
        self.velocity = pygame.math.Vector2(velocity)
    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
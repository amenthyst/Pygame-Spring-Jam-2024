import pygame
import images
import tags

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        super().__init__()
        self.image = images.renderbullet()
        self.rect = self.image.get_rect(center=position)
        self.velocity = pygame.math.Vector2(velocity)
        self.damage = 1
    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def on_collide(self, other):
        if other is not tags.Damageable:
            return
        other.damage(self.damage)
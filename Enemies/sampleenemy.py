from Objects import tags
import pygame
import images
class Enemy(pygame.sprite.Sprite, tags.Damageable):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.image = pygame.transform.scale(images.renderbullets()[0], (100,100))
        self.rect = self.image.get_rect(center=self.pos)

    def damage(self, amount):
        print("damaged", amount)


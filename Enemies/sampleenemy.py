from Objects import tags
import pygame
import images
class Enemy(pygame.sprite.Sprite, tags.Damageable):



    def __init__(self, pos, health, dmg, speed, size):

        super().__init__()
        self.pos = pos
        self.maxhealth = health
        self.health = health
        self.dmg = dmg
        self.speed = speed
        self.size = size
        self.image = pygame.transform.scale(images.renderbullets()[0], self.size)
        self.rect = self.image.get_rect(center=self.pos)
        

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.healthbar(screen)
    def healthbar(self, screen):
        pygame.draw.rect(screen, "black", (self.rect.x-3, self.rect.y-15, self.size[0] ,10), 2)
        ratio = self.health/self.maxhealth
        pygame.draw.rect(screen, "green", (self.rect.x-1, self.rect.y-13, self.size[0]*ratio-4, 6))

    def attack(self):
        pass

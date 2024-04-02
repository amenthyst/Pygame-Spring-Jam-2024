from sampleenemy import Enemy
import pygame
from Objects.player import Player
from Objects import tags
class Basher(pygame.sprite.Sprite, Enemy):
    def __init__(self, pos: tuple, health, speed, dmg, image, size: tuple):
        super().__init__(pos, health, dmg, speed)
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(pos)
        self.confuseflag = False
    def move(self):
        if not self.confuseflag:
            self.targetpos = Player.Instance.get_centre()
            self.direction = self.pos - self.targetpos
            if self.direction.length():
                self.direction.normalize_ip()

            self.direction *= self.speed

            self.rect.x += self.direction.x
            self.rect.y += self.direction.y

    def attack(self):
        if self.rect.colliderect(Player.Instance.rect):
            Player.Instance.damage()






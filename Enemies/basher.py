from Enemies.sampleenemy import Enemy
import pygame
from Objects.player import Player
import images
from Objects import tags
class Basher(Enemy, pygame.sprite.Sprite):
    def __init__(self, pos: tuple, health, speed, dmg, size: tuple, state):
        super().__init__(pos, health, dmg, speed, state, size)
        if self.state == "hot":
            self.image = pygame.transform.scale(images.renderenemies()[0], size)
        elif self.state == "cold":
            self.image = pygame.transform.scale(images.renderenemies()[1], size)
        self.rect = self.image.get_rect(center=pos)
        self.confuseflag = False

    def move(self):
        self.targetpos = Player.Instance.get_centre()
        self.pos = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.direction = self.targetpos - self.pos

        if self.direction.length():
            self.direction.normalize_ip()

        self.direction *= self.speed

        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def attack(self):
        if self.rect.colliderect(Player.Instance.rect):
            Player.Instance.damage(self.dmg)
            self.kill()


    def update(self, dt):
        self.attack()
        self.move()







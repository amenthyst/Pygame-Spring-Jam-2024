import pygame
import images
import math
from Objects.player import Player
from Objects.particle import Particle
class Enemybullet(pygame.sprite.Sprite):
    def __init__(self, direction: pygame.math.Vector2, pos, speed, dmg, state, bulletgrp):
        super().__init__()
        self.state = state
        if self.state == "hot":
            self.image = images.renderenemies()[3]
        elif self.state == "cold":
            self.image = images.renderenemies()[2]

        self.image = pygame.transform.rotate(self.image, self.getangle(direction)-90)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.speed = speed
        self.dmg = dmg
        self.bulletgrp = bulletgrp
        self.border = pygame.Rect(0,0,1000,600)

    def getangle(self, direction):
        return math.degrees(math.atan2(direction.x, direction.y))

    def move(self):
        self.direction.normalize_ip()
        self.velocity = -(self.speed * self.direction)

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect not in self.border:
            self.kill()


    def attack(self):
        if self.rect.colliderect(Player.Instance.rect):
            Player.Instance.damage(self.dmg)
            self.kill()

    def update(self, dt):
        self.move()
        self.attack()
        self.shock()

    def shock(self):
        hitlist = pygame.sprite.spritecollide(self, self.bulletgrp, False)
        for obj in hitlist:
            if not isinstance(obj, Particle):
                continue
            if obj.state == "shock":
                obj.kill()
                self.kill()




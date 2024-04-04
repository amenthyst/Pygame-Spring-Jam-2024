import pygame
import images
from Objects.player import Player
from Enemies.sampleenemy import Enemy
from Enemies.enemybullet import Enemybullet
import random
class Shooter(Enemy, pygame.sprite.Sprite):
    def __init__(self, pos, health, speed, dmg, size, state, bulletgrp):
        super().__init__(pos, health, dmg, speed, state, size, bulletgrp)
        if self.state == "hot":
            self.image = images.renderenemies()[4]
        elif self.state == "cold":
            self.image = images.renderenemies()[5]

        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.shootcooldown = random.uniform(1,3)
        self.shoottimer = 0
        self.moving = True
        self.target = pygame.math.Vector2(random.uniform(200, 800), random.uniform(100, 500))

    def move(self):

        if not self.confusion:
            self.pos = pygame.math.Vector2(self.rect.x, self.rect.y)


            self.direction = self.target - self.pos

            if self.direction.length():
                self.direction.normalize_ip()

            self.velocity = self.direction * self.speed

            self.rect.x += self.velocity.x
            self.rect.y += self.velocity.y

            if self.pos == self.target:
                self.moving = False

        else:

            # makes it vibrate
            self.direction = pygame.math.Vector2(random.uniform(-5,5), random.uniform(-5,5))
            self.direction.normalize_ip()

            self.direction *= self.speed


            self.rect.x += self.direction[0]
            self.rect.y += self.direction[1]

    def shoot(self, dt):
        self.shoottimer += dt
        if self.shoottimer < self.shootcooldown:
            return
        self.shoottimer = 0
        self.bulletgrp.add(Enemybullet(self.pos-Player.Instance.get_centre(), self.pos, 5, 5, self.state, self.bulletgrp))


    def update(self, dt):
        if self.moving:
            self.move()
        if not self.confusion:
            self.shoot(dt)

        self.confuse(dt)

    def draw(self, screen):
        if self.moving:
            self.rotimage = pygame.transform.rotate(self.image, self.getangle(self.pos - Player.Instance.get_centre()))
            self.rotrect = self.rotimage.get_rect(center=self.pos)

            screen.blit(self.rotimage, self.rotrect)
            self.rothealthbar(screen)
        else:
            screen.blit(self.image, self.rect)
            self.healthbar(screen)

    def rothealthbar(self, screen):
        pygame.draw.rect(screen, "black", (self.rotrect.x - 3, self.rotrect.y - 15, self.size[0], 10), 2)
        ratio = self.health / self.maxhealth
        pygame.draw.rect(screen, "green", (self.rotrect.x - 1, self.rotrect.y - 13, self.size[0] * ratio - 4, 6))



import pygame
import random
from Objects import tags
class Particle(pygame.sprite.Sprite):


    def __init__(self, state, bulletgrp: pygame.sprite.Group, pos: tuple):
        super().__init__(bulletgrp)

        self.hotlist = ((255,0,0), (255,128,0), (255,255,0))

        self.coldlist = ((51,255,255), (0,255,255), (153,204,255))

        self.state = state

        self.originalpos = pygame.math.Vector2(0,0)

        self.pos = pygame.math.Vector2(pos)

        if self.state == "hot":
            self.color = random.choice(self.hotlist)
        elif self.state == "cold":
            self.color = random.choice(self.coldlist)

        self.speed = random.uniform(15,15.5)

        self.direction = pygame.math.Vector2(random.uniform(-1,1), random.uniform(-1,1))

        self.damage = 0.05

        self.radius = 75

        self.createsurf()

    def createsurf(self):
        self.image = pygame.Surface((6,6)).convert_alpha()
        self.image.set_colorkey("black")
        pygame.draw.circle(self.image, self.color, center=(2, 2), radius=8)
        self.rect = self.image.get_rect(center=self.pos)
    def on_collide(self, other):
        if not isinstance(other, tags.Damageable):
            return
        other.damage(self.damage)

    def move(self):
        self.velocity = self.direction * self.speed

        self.originalpos += self.velocity

        self.pos += self.velocity
        if self.originalpos.magnitude() > self.radius:
            self.kill()
        self.rect.center = self.pos


    def update(self, dt):
        self.move()
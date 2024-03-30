import pygame
import random
from Objects import tags
class Particle(pygame.sprite.Sprite):


    def __init__(self, state, bulletgrp: pygame.sprite.Group, pos: tuple, radius):
        super().__init__(bulletgrp)

        self.hotlist = ((255,0,0), (255,128,0), (255,255,0), (253,67,38), (247,77,77))

        self.coldlist = ((51,255,255), (0,255,255), (153,204,255), (161,246,238), (104,203,239))

        self.state = state

        self.originalpos = pygame.math.Vector2(0,0)

        self.pos = pygame.math.Vector2(pos)

        if self.state == "hot":
            self.color = random.choice(self.hotlist)
        elif self.state == "cold":
            self.color = random.choice(self.coldlist)


        self.speed = 100

        self.speed = 10

        self.direction = pygame.math.Vector2(random.uniform(-1,1), random.uniform(-1,1))

        self.damage = 0.05

        self.radius = radius

        self.duration = 1

        self.timer = 0

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

    def move(self, dt):
        self.timer += dt

        if self.timer > self.duration:
            self.kill()

        self.velocity = self.direction * self.speed

        self.originalpos += self.velocity

        self.pos += self.velocity
        if self.originalpos.magnitude() > self.radius:
            self.kill()
        self.rect.center = self.pos


    def update(self, dt):
        self.move(dt)
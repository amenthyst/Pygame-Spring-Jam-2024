import pygame
import random
from Objects import tags
class Particle(pygame.sprite.Sprite):
    particles = []
    MAX_PARTICLES = 600

    def __new__(cls, *args, **kwargs):
        if len(Particle.particles) > Particle.MAX_PARTICLES:
            next = Particle.particles[0]
            Particle.particles.pop(0)
            Particle.particles.append(next)
            return next
        particle = super().__new__(cls)
        Particle.particles.append(particle)
        return particle

    def __init__(self, state, mode, enemygrp: pygame.sprite.Group, bulletgrp: pygame.sprite.Group, speed, pos: tuple, direction: pygame.math.Vector2, radius, duration, damage):
        super().__init__(bulletgrp)
        self.initialize(state, mode, enemygrp, bulletgrp, speed, pos, direction, radius, duration, damage)

    def initialize(self, state, mode, enemygrp: pygame.sprite.Group, bulletgrp: pygame.sprite.Group, speed, pos: tuple, direction: pygame.math.Vector2, radius, duration, damage):
        self.hotlist = ((255,0,0), (255,128,0), (255,255,0), (253,67,38), (247,77,77))

        self.coldlist = ((51,255,255), (0,255,255), (153,204,255), (161,246,238), (104,203,239))

        self.steamlist = ((221,223,224), (194,197,198), (242,250,253), (205,211,213), (177,186,189))

        self.state = state

        self.originalpos = pygame.math.Vector2(0,0)

        self.pos = pygame.math.Vector2(pos)

        self.enemygrp = enemygrp

        self.bulletgrp = bulletgrp

        if self.state == "hot":
            self.color = random.choice(self.hotlist)
        elif self.state == "cold":
            self.color = random.choice(self.coldlist)
        elif self.state == "steam":
            self.color = random.choice(self.steamlist)


        self.speed = speed


        self.mode = mode

        if self.mode == "ball":
            self.direction = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        elif self.mode == "cone":
            self.direction = direction
            self.direction = self.direction.rotate(random.uniform(-175,-185))
            self.direction = self.direction.normalize()
            self.speed = random.uniform(5,10)


        self.damage = damage

        self.range = radius

        self.duration = duration


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
        if self.state != "steam":
            self.kill()

    def move(self, dt):
        self.timer += dt

        if self.timer > self.duration:
            self.kill()

        self.velocity = self.direction * self.speed

        self.originalpos += self.velocity

        self.pos += self.velocity
        if self.originalpos.magnitude() > self.range and self.mode == "ball":
            self.kill()
        self.rect.center = self.pos


    def steam(self):
        hitlist = pygame.sprite.spritecollide(self, self.bulletgrp, False)
        for obj in hitlist:
            if not isinstance(obj, Particle):
                continue
            if (obj.state == "hot" and self.state == "cold") or (obj.state == "cold" and self.state == "hot"):
                self.bulletgrp.add(Particle("steam", "ball", self.enemygrp, self.bulletgrp, 0.25, self.pos, None, 300, 10, 0))
                self.kill()
                obj.kill()

    def attack(self):
        hitlist = pygame.sprite.spritecollide(self, self.enemygrp, False)
        for obj in hitlist:
            self.on_collide(obj)

    def update(self, dt):
        self.steam()
        self.move(dt)
        self.attack()

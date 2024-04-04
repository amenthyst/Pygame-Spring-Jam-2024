import pygame
import Systems.input
import math
from Objects import tags
class Player(pygame.sprite.Sprite, tags.Damageable):
    Instance = None
    def __init__(self, playertuple, position, speed, bullet, bomb, particle, bullet_group, enemygrp, health):
        # singleton
        if Player.Instance != None:
            raise Exception("Multiple Player instances! :(")
        Player.Instance = self

        super().__init__()
        self.state = "cold"

        self.firesprite = playertuple[0]
        self.icesprite = playertuple[1]

        self.checktexture()
        self.rect = self.image.get_rect(center=position)

        self.velocity = pygame.math.Vector2()

        self.recoilvelocity = pygame.math.Vector2()

        self.friction = 0.845
        self.maxvelocity = 20
        self.acceleration = speed
        self.bulletlastframe = False

        self.bullet = bullet
        self.bomb = bomb
        self.particle = particle

        self.shoot_force = 20
        self.bulletgrp = bullet_group
        self.enemygrp = enemygrp
        self.shoot_cooldown = 0.33
        self.bomb_cooldown = 1.5
        self.bomb_timer = 0
        self.shoot_timer = 0

        self.max_dodges = 2
        self.remaining_dodges = 2
        self.dodge_time = 0.085
        self.dodge_timer = 0
        self.dodging = False
        self.dodge_dir = pygame.math.Vector2(0, 0)
        self.dodge_speed = 40
        self.dodge_lag = 0.3
        self.dodge_lag_timer = 0.3
        self.locked = False
        self.dodge_regen_time = 3
        self.dodge_regen_timer = 0

        self.changing = False

        self.health = health
        self.maxhealth = health
        self.size = (75,75)

        self.totaldamage = 0

        self.border = pygame.Rect(0,0,1000,600)

        self.mana = 1

        self.cancast = True

        self.invincibility = False

        self.invincibilitytime = 0.1

        self.invintimer = 0

    def get_pos(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self.rect.x, self.rect.y)
    def get_centre(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self.rect.centerx, self.rect.centery)

    def move(self):
        if self.dodge_lag_timer < self.dodge_lag:
            return
        if self.dodging:
            return


        dir = Systems.input.get_vector(pygame.K_a, pygame.K_d,
                                       pygame.K_w, pygame.K_s)

        self.rect.clamp_ip(self.border)
        if dir.length() > 0:
            self.velocity += dir.normalize() * self.acceleration

        if self.velocity.magnitude() > self.maxvelocity:
            self.velocity = self.velocity.normalize() * self.maxvelocity

    def handle_physics(self):
        self.velocity *= self.friction

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def shoot(self, dt):
        self.shoot_timer += dt * (2 if self.locked else 1)
        if not pygame.mouse.get_pressed(3)[0]:
            return
        if self.shoot_timer < self.shoot_cooldown:
            return
        self.shoot_timer = 0
        mouse_pos = pygame.mouse.get_pos()
        bullet_dir = pygame.math.Vector2(mouse_pos) - self.get_centre()
        bullet_dir = bullet_dir.normalize()
        bullet = self.bullet(self.get_centre(), bullet_dir * self.shoot_force, self.enemygrp, self.state)
        self.bulletgrp.add(bullet)
    def shootbomb(self, dt):
        self.bomb_timer += dt * (2 if self.locked else 1)
        if not pygame.mouse.get_pressed(3)[2]:
            return
        if self.bomb_timer < self.bomb_cooldown:
            return
        self.bomb_timer = 0
        mouse_pos = pygame.mouse.get_pos()
        bombdir = pygame.math.Vector2(mouse_pos) - self.get_centre()
        bombdir = bombdir.normalize()
        bomb = self.bomb(self.get_centre(), bombdir * self.shoot_force, self.bulletgrp, self.enemygrp, self.state)
        self.bulletgrp.add(bomb)


    def thrower(self, dt):

        if Systems.input.is_key_held(pygame.K_f) and self.mana > 0 and self.cancast:
            for _ in range(0,3):
                particledir = -(pygame.math.Vector2(pygame.mouse.get_pos()) - self.get_centre())
                particle = self.particle(self.state, "cone", self.enemygrp, self.bulletgrp, 5, self.get_centre(), particledir, 200, 0.6, 0.02)
                self.bulletgrp.add(particle)
                self.mana -= dt / 5

            if self.mana < 0:
                self.mana = 0
                self.cancast = False







    def update(self, dt):
        self.checktexture()
        self.rotimage = pygame.transform.rotate(self.image, self.getangle())
        self.rotrect = self.rotimage.get_rect(center=tuple(self.get_centre()))
        self.move()
        self.shoot(dt)
        self.shootbomb(dt)
        self.thrower(dt)
        self.shockwave()
        self.dodge(dt)
        self.handle_physics()
        if self.changing:
            self.totaldamage = 0




    def recoil(self):
        # most annoying thing known to man
        particledir = self.get_centre() - pygame.mouse.get_pos()
        self.recoilvelocity += particledir * self.acceleration/20

        if self.recoilvelocity.length():
            self.recoilvelocity.normalize_ip()

        if self.recoilvelocity.magnitude() > self.maxvelocity/20:
            self.recoilvelocity = self.recoilvelocity.normalize() * self.maxvelocity/20

        self.recoilvelocity *= self.friction

        self.rect.x += self.recoilvelocity[0]
        self.rect.y += self.recoilvelocity[1]


    def dodge(self, dt):
        dodge_dir = Systems.input.get_vector(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
        if dodge_dir != pygame.math.Vector2(0, 0):
            self.dodge_dir = dodge_dir

        if not self.dodging and not self.locked and self.remaining_dodges < self.max_dodges:

            self.dodge_regen_timer += dt
            if self.dodge_regen_timer >= self.dodge_regen_time:
                self.remaining_dodges += 1
                self.dodge_regen_timer = 0

        if self.dodging:

            if self.dodge_dir.length():
                self.velocity = self.dodge_dir.normalize() * self.dodge_speed
            self.dodge_timer += dt
            if self.dodge_timer >= self.dodge_time:
                self.dodging = False
                self.velocity = pygame.math.Vector2(0, 0)
                self.locked = True
            return
        if self.locked:
            self.dodge_lag_timer += dt
            # timer for invincibility
            self.invintimer += dt
            if self.invintimer > self.invincibilitytime:
                self.invincibility = False
                self.invintimer = 0
            if self.velocity.length() > 0:
                self.locked = False
        if Systems.input.is_key_just_pressed(pygame.K_LSHIFT) and not self.dodging and self.remaining_dodges > 0:
            self.dodging = True
            self.remaining_dodges -= 1
            self.dodge_timer = 0
            self.dodge_lag_timer = 0
            self.invincibility = True


    def getangle(self):
        direction = pygame.math.Vector2(pygame.mouse.get_pos()) - self.get_centre()
        return math.degrees(math.atan2(direction.x, direction.y)) + 180

    def draw(self, screen, dt):
        screen.blit(self.rotimage, self.rotrect)
        self.healthbar(screen)
        self.cooldownbar(screen, dt)

    def checktexture(self):
        if self.state == "hot":
            self.image = self.firesprite
        elif self.state == "cold":
            self.image = self.icesprite


    def damage(self, amount: int):
        if not self.invincibility:
            self.health -= amount
        if self.health <= 0:
            self.totaldamage = 0
            self.kill()

    def healthbar(self, screen):
        pygame.draw.rect(screen, "black", (self.rect.x - 3, self.rect.y - 15, self.size[0], 10), 2)
        ratio = self.health / self.maxhealth
        pygame.draw.rect(screen, "green", (self.rect.x - 1, self.rect.y - 13, self.size[0] * ratio - 4, 6))

    def addtotaldamage(self, amount):
        self.totaldamage += amount

    def heal(self, amount):
        self.health += amount
        if self.health > self.maxhealth:
            self.health = self.maxhealth

    def cooldownbar(self, screen, dt):
        pygame.draw.rect(screen, "black", (self.rect.x - 3, self.rect.y + 80, self.size[0], 10), 2)
        pygame.draw.rect(screen, "white", (self.rect.x - 1, self.rect.y + 82, self.size[0] * self.mana - 4, 6))

        if not self.cancast:
            self.cancast = False
            self.mana += dt / 3
            if self.mana > 1:
                self.cancast = True


    def shockwave(self):
        if Systems.input.is_key_just_pressed(pygame.K_r) and self.mana > 0 and self.cancast:
            for _ in range(0,75):
                self.bulletgrp.add(self.particle("shock", "ball", self.enemygrp, self.bulletgrp, 5, self.get_centre(), None, 125, 0.75, 0))
            self.mana -= 0.25
            if self.mana <= 0:
                self.mana = 0
                self.cancast = False













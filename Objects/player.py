import pygame
import Systems.input


class Player(pygame.sprite.Sprite):
    def __init__(self, playersurf, position, speed, bullet, bomb, particle, bullet_group, enemygrp):
        super().__init__()
        self.image = playersurf
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
        self.bomb_cooldown = 0.33
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
        self.dodge_regen_time = 2
        self.dodge_regen_timer = 0

    def get_pos(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self.rect.x, self.rect.y)
    def get_centre(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self.rect.centerx, self.rect.centery)

    def move(self):
        if self.dodge_lag_timer < self.dodge_lag:
            return
        if self.dodging:
            return

        pressed = Systems.input.get_pressed()

        dir = Systems.input.get_vector(pygame.K_a, pygame.K_d,
                                       pygame.K_w, pygame.K_s)
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
        bullet = self.bullet(self.get_centre(), bullet_dir * self.shoot_force, self.enemygrp)
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
        bomb = self.bomb(self.get_centre(), bombdir * self.shoot_force, self.bulletgrp, self.enemygrp)
        self.bulletgrp.add(bomb)


    def thrower(self, dt):
        keys = Systems.input.get_pressed()
        if not keys[pygame.K_f]:
            return
        for _ in range(0,3):
            particledir = -(pygame.math.Vector2(pygame.mouse.get_pos()) - self.get_centre())
            particle = self.particle("hot", "cone", self.enemygrp, self.bulletgrp, 5, self.get_centre(), particledir, 300, 0.6, 0.02)
            self.bulletgrp.add(particle)


    def update(self, dt):
        self.move()
        self.shoot(dt)
        self.shootbomb(dt)
        self.thrower(dt)
        self.dodge(dt)
        self.handle_physics()

    def recoil(self):

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
            print("dodging", self.dodge_dir)
            self.velocity = self.dodge_dir.normalize() * self.dodge_speed
            self.dodge_timer += dt
            if self.dodge_timer >= self.dodge_time:
                self.dodging = False
                self.velocity = pygame.math.Vector2(0, 0)
                self.locked = True
            return
        if self.locked:
            print("locked")
            self.dodge_lag_timer += dt
            if self.velocity.length() > 0:
                self.locked = False
        if Systems.input.is_key_just_pressed(pygame.K_LSHIFT) and not self.dodging and self.remaining_dodges > 0:
            print("dodge")
            self.dodging = True
            self.remaining_dodges -= 1
            self.dodge_timer = 0
            self.dodge_lag_timer = 0
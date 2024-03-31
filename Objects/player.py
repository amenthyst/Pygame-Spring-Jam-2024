import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, playersurf, position, speed, bullet, bomb, particle, bullet_group, enemygrp):
        super().__init__()
        self.image = playersurf
        self.rect = self.image.get_rect(center=position)

        self.velocity = pygame.math.Vector2()
        self.controls = {pygame.K_w: (0, -1),
                         pygame.K_s: (0, 1),
                         pygame.K_a: (-1, 0),
                         pygame.K_d: (1, 0)}
        self.friction = 0.845
        self.maxvelocity = 20
        self.acceleration = speed

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

    def get_pos(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self.rect.x, self.rect.y)
    def get_centre(self) -> pygame.math.Vector2:
        return pygame.math.Vector2(self.rect.centerx, self.rect.centery)

    def move(self):
        pressed = pygame.key.get_pressed()


        for vec in (self.controls[k] for k in self.controls if pressed[k]):

            self.velocity += pygame.math.Vector2(vec) * self.acceleration

        if self.velocity.magnitude() > self.maxvelocity:
            self.velocity = self.velocity.normalize() * self.maxvelocity


        self.velocity *= self.friction


        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def shoot(self, dt):
        self.shoot_timer += dt # i rly dont like this but theres no way to get delta yet
        if not pygame.mouse.get_pressed(3)[0]:
            return
        if self.shoot_timer < self.shoot_cooldown:
            return
        self.shoot_timer = 0
        mouse_pos = pygame.mouse.get_pos()
        bullet_dir = pygame.math.Vector2(mouse_pos) - self.get_centre()
        bullet_dir = bullet_dir.normalize()
        bullet = self.bullet(self.get_centre(), bullet_dir * self.shoot_force)
        self.bulletgrp.add(bullet)

    def shootbomb(self, dt):
        self.bomb_timer += dt
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
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_f]:
            return
        for _ in range(0,5):
            particledir = -(pygame.math.Vector2(pygame.mouse.get_pos()) - self.get_centre())
            particle = self.particle("hot", "cone", self.bulletgrp, 5, self.get_centre(), particledir, 300, 0.6)
            self.bulletgrp.add(particle)
    def update(self, dt):
        self.move()
        self.shoot(dt)
        self.shootbomb(dt)
        self.thrower(dt)









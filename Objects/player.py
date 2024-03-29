import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, playersurf, position, speed, bullet, bullet_group):
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
        self.shoot_force = 10
        self.bulletgrp = bullet_group
        self.shoot_cooldown = 0.1
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

    def shoot(self):
        self.shoot_timer += 1 / 60 # i rly dont like this but theres no way to get delta yet
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

    def update(self):
        self.move()
        self.shoot()










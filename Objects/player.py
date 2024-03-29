import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, playersurf, position, speed):
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
        pass
    def update(self):
        self.move()










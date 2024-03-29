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
        self.deceleration = 0.93
        self.maxvelocity = 40
        self.speed = speed


    def move(self):
        pressed = pygame.key.get_pressed()

        for vec in (self.controls[k] for k in self.controls if pressed[k]):
            self.velocity += vec
            self.velocity *= self.speed

        if self.velocity.magnitude() > self.maxvelocity:
            self.velocity = self.velocity.normalize() * self.maxvelocity


        self.velocity *= self.deceleration


        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def update(self):
        self.move()










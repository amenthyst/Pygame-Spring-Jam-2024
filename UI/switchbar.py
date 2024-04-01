import pygame
import images
# this thing switches between hot and cold
class Switchbar(pygame.sprite.Sprite):

    def __init__(self, player, pos, duration):
        super().__init__()
        self.player = player
        self.pos = pygame.math.Vector2(pos)
        self.duration = duration
        self.ratio = 0
        self.ice = pygame.transform.scale(images.renderbullets()[0], (60,60))
        self.fire = pygame.transform.scale(images.renderbullets()[1], (60,60))
    def draw(self, screen):
        if self.player.state == "hot":
            self.color = (255,128,0)

        elif self.player.state == "cold":
            self.color = (51,255,255)


        pygame.draw.rect(screen, "black", (self.pos.x, self.pos.y, 225, 40), 6)
        pygame.draw.rect(screen, self.color, (self.pos.x+6, self.pos.y+6, 225*self.ratio, 28))

        if self.player.state == "hot":
            screen.blit(self.fire, (self.pos.x-20, self.pos.y-9))
        elif self.player.state == "cold":
            screen.blit(self.ice, (self.pos.x-20, self.pos.y-9))


    def switch(self, dt):
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_q]:
            return
        self.ratio += dt
        if self.ratio >= 0.95:
            self.ratio = 0
            if self.player.state == "hot":
                self.player.state = "cold"
            elif self.player.state == "cold":
                self.player.state = "hot"
            self.player.changing = True

    def update(self, dt):
        self.switch(dt)
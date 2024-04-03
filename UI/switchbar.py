import pygame
import images
from Objects.player import Player
from UI.wavecounter import Wavecounter
import Systems
# this thing switches between hot and cold
class Switchbar(pygame.sprite.Sprite):

    def __init__(self, pos, duration):
        super().__init__()
        self.pos = pygame.math.Vector2(pos)
        self.duration = duration
        self.ratio = 0
        self.ice = pygame.transform.scale(images.renderbullets()[0], (60,60))
        self.fire = pygame.transform.scale(images.renderbullets()[1], (60,60))
        self.damagereq = 10
        self.font = pygame.font.Font("Graphics/font.otf", 25)
    def draw(self, screen):
        self.player = Player.Instance
        if self.player.state == "hot":
            self.color = (255,128,0)

        elif self.player.state == "cold":
            self.color = (51,255,255)

        text = self.font.render("SWITCH!", False, "black")
        pygame.draw.rect(screen, "black", (self.pos.x, self.pos.y, 225, 40), 6)
        pygame.draw.rect(screen, self.color, (self.pos.x+6, self.pos.y+6, 225*self.ratio, 28))

        if self.player.state == "hot":
            screen.blit(self.fire, (self.pos.x-20, self.pos.y-9))
        elif self.player.state == "cold":
            screen.blit(self.ice, (self.pos.x-20, self.pos.y-9))

        if self.ratio >= 0.95:
              screen.blit(text, (752, 53))

    def switch(self, dt):
        self.ratio += Player.Instance.totaldamage / self.damagereq

        Player.Instance.totaldamage = 0
        if self.ratio >= 0.95:
            self.ratio = 0.95
            if Systems.input.is_key_just_pressed(pygame.K_q):
                self.ratio = 0
                if self.player.state == "hot":
                    self.player.state = "cold"
                elif self.player.state == "cold":
                    self.player.state = "hot"
                self.player.changing = True
                Player.Instance.health = 100

    def update(self, dt):
        self.damagereq = Wavecounter.Instance.currentwave * 7 + 1
        self.switch(dt)

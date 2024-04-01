import pygame
import images
import math
class Background(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.ice = images.renderbullets()[0]
        self.fire = images.renderbullets()[1]

        self.bg = images.renderbackground()
        self.bgrect = self.bg.get_rect(topleft=(0,0))


        self.player = player

        self.transitionlist = []

        self.transitioned = False



    def draw(self, screen):

        screen.blit(self.bg, self.bgrect)
        for rect in self.transitionlist:
            screen.blit(self.image, rect)

        print(self.bgrect.y)
    def transition(self):
        self.changing = self.player.changing

        self.state = self.player.state

        if not self.changing:
            return



        if self.state == "hot" and not self.transitioned:

            self.image = self.fire
            for i in range(0,100):
                self.firerect = self.image.get_rect(center=(i*12, 600))
                self.transitionlist.append(self.firerect)
            self.transitioned = True


        elif self.state == "cold" and not self.transitioned:
            self.image = self.ice
            for i in range(0,100):
                self.icerect = self.image.get_rect(center=(i*12, 0))
                self.transitionlist.append(self.icerect)
            self.transitioned = True




        if self.state == "hot":
            self.bgrect.y = 0
            for item in self.transitionlist:
                self.bgrect.y = item.y-600
                item.y -= 8

                if self.bgrect.y < -594:
                    self.transitionlist = []
                    self.player.changing = False
                    self.transitioned = False


        elif self.state == "cold":
            for item in self.transitionlist:
                self.bgrect.y = item.y-600
                item.y += 8
                if self.bgrect.y > 0:
                    self.transitionlist = []
                    self.player.changing = False
                    self.transitioned = False




    def update(self, dt):
        self.transition()

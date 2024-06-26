import pygame
import images
import math
from Objects.player import Player
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ice = pygame.transform.scale(images.renderbullets()[0], (32,32))
        self.fire = pygame.transform.scale(images.renderbullets()[1], (32,32))

        self.bg = images.renderbackground()
        self.bgrect = self.bg.get_rect(topleft=(0,0))



        self.transitionlist = []

        self.transitioned = False



    def draw(self, screen):

        screen.blit(self.bg, self.bgrect)
        for rect in self.transitionlist:
            screen.blit(self.image, rect)


    def transition(self):

        self.player = Player.Instance

        self.changing = self.player.changing

        self.state = self.player.state

        if not self.changing:
            return



        if self.state == "hot" and not self.transitioned:

            self.image = self.fire
            for i in range(0,50):
                self.firerect = self.image.get_rect(center=(i*26, 600))
                self.transitionlist.append(self.firerect)
            self.transitioned = True


        elif self.state == "cold" and not self.transitioned:
            self.image = self.ice
            for i in range(0,50):

                self.icerect = self.image.get_rect(center=(i*26, 0))


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

                self.bgrect.y = item.y-572
                item.y += 8

                if self.bgrect.y > 0:

                    self.transitionlist = []
                    self.player.changing = False
                    self.transitioned = False




    def update(self, dt):
        self.transition()

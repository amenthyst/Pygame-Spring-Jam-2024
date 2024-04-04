import pygame
import Systems.input as input


class Button(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], sprite: pygame.surface.Surface, on_clicked) -> None:
        super().__init__()
        self.original_image = sprite
        self.image = sprite.copy()
        self.rect = self.image.get_rect(center=position)
        self.on_clicked = on_clicked

    def update(self) -> None:
        if self.rect.collidepoint(input.get_pos()):
            self.on_hover()
        else:
            self.image = self.original_image.copy()

    def on_hover(self):
        self.image = self.original_image.copy()
        self.image.fill((100, 100, 100, 100), special_flags=pygame.BLEND_ADD)
        if input.l_pressed():
            self.on_clicked()

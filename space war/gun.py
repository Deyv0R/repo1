import pygame
from pygame.sprite import Sprite

class Gun(Sprite):

    def __init__(self, screen):    # ініціалізація пушки
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('space war\image for game\pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):        # малювання пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self):        # оновлення позиції пушки
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.1
        elif self.mleft and self.rect.left > 0:
            self.center -= 1.1

        self.rect.centerx = self.center

    def create_gun(self):       # розміщує пушку по центру в нижній частині екрану
        self.center = self.screen_rect.centerx

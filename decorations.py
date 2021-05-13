import pygame
from pygame.sprite import Sprite

class Decorations(Sprite):
    def __init__(self, screen, sp):
        super().__init__()
        self.setting = sp
        self.screen = screen
        self.image = pygame.image.load('images/decorations.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 1000
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx -= self.setting.decorations_speed

        if self.rect.right < 0:  
            self.rect.left = 1200

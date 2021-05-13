import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self, screen, sp):
        super().__init__()
        self.setting = sp
        self.screen = screen
        self.image = pygame.image.load('images/background.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 1500
        self.rect.bottom = self.screen_rect.bottom

    def second_background(self):
        self.rect.centerx = 4500

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.centerx -= self.setting.background_speed

        if self.rect.centerx < -1500:  
            self.rect.centerx = 4500

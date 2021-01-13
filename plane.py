import pygame
from pygame.sprite import Sprite

class Plane(Sprite):
    def __init__(self, screen, sp):
        super().__init__()
        self.setting = sp
        self.screen = screen
        self.image = pygame.image.load('images/rocet.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.rect.size[0] / 2
        self.rect.centery = self.screen_rect.size[1] / 2
        self.movingup = False
        self.hp = sp.player_hp
        self.movingdown = False

    def secondplayer(self):
        self.image = pygame.image.load('images/rocet2.bmp')
        self.rect.centerx = self.screen_rect.right - self.rect.size[0]
        self.rect.centery = self.screen_rect.size[1] / 2

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.movingup is True and self.rect.centery > (self.rect.size[1] / 4):
            self.rect.centery -= self.setting.player_speed
        if self.movingdown is True and self.rect.centery < self.screen_rect.size[1] - (self.rect.size[1] / 4):
            self.rect.centery += self.setting.player_speed
        if self.hp <= 0:
            print("Im dead")

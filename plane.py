import pygame
from pygame.sprite import Sprite

class Plane(Sprite):
    def __init__(self, screen, sp):
        super().__init__()
        self.setting = sp
        self.screen = screen
        self.image = pygame.image.load('images/plane1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.rect.size[0] / 2
        self.rect.centery = self.screen_rect.size[1] / 2
        self.movingup = False
        self.hp = sp.player_hp
        self.movingdown = False

        self.moving_speed = 0
        self.bullets_number = 0

    def secondplayer(self):
        self.image = pygame.image.load('images/plane2.bmp')
        self.rect.centerx = self.screen_rect.right - self.rect.size[0] / 2
        self.rect.centery = self.screen_rect.size[1] / 2

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self):

        if self.movingup is True:
            self.moving_speed += self.setting.player_acc
        if self.movingdown is True:
            self.moving_speed -= self.setting.player_acc
        
        if self.rect.top - self.moving_speed + 60 < 0 or self.rect.bottom - self.moving_speed - 60 > self.screen_rect.size[1]:
            self.moving_speed = 0
        
        self.rect.centery -= self.moving_speed

        if self.hp <= 0:
            print("Im dead")

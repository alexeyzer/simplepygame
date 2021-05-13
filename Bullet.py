import pygame
from pygame.sprite import Sprite

class bullet(Sprite):
    def __init__(self, screen, sp, ship):
        super().__init__()
        self.screen = screen
        self.ship = ship
        self.rect = pygame.Rect(0, 0, sp.bullet_width, sp.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.centerx
        self.x = float(self.rect.x)
        self.color = sp.bullet_color
        self.speed = sp.bullet_speed
    def update(self):
        self.x += self.speed
        self.rect.x = self.x
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

import pygame

class Text():
    def __init__(self, screen, str):
        self.text = str
        self.screen = screen
        self.font = pygame.font.SysFont('None', 40)
        self.update()
        self.rect.centerx = screen.get_rect().centerx
        self.rect.centery = screen.get_rect().centery
    def update(self):
        self.surface = self.font.render(self.text, True, (0, 0, 0))
        self.rect = self.surface.get_rect()


    def blitme(self):
        self.screen.blit(self.surface, self.rect)

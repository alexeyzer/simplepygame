import pygame
import sys
from settings import Settings
from text import Text
from plane import Plane
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    pygame.font.init()
    sp = Settings()
    bullets = Group()
    screen = pygame.display.set_mode((sp.screen_width, sp.screen_height))
    player = Plane(screen, sp)
    player2 = Plane(screen, sp)
    player2.secondplayer()
    working = True
    text = None

    while working:
        gf.check_events(player, player2, bullets, screen, sp)
        player.update()
        player2.update()
        text = gf.check_dead(player, player2, screen)
        if text is not None:
            working = False
        gf.update_bullet(bullets, player, player2)
        gf.update_screen(sp, screen, player, player2, bullets, text)
    working = True
    while working:
        gf.check_events(player, player2, bullets, screen, sp)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

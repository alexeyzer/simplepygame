import pygame
import sys
from Bullet import bullet
from pygame.locals import *
from text import Text

def check_keyup_event(event, ship1, ship2):
    if event.key == K_w:
        ship1.movingup = False
    elif event.key == K_UP:
        ship2.movingup = False
    elif event.key == K_s:
        ship1.movingdown = False
    elif event.key == K_DOWN:
        ship2.movingdown = False

def check_keydown_event(event, ship1, ship2, bullets, screen, sp):
    if event.key == K_ESCAPE:
        sys.exit()
    elif event.key == K_f:
        fire_bullet(screen, sp, ship1, bullets, 0)
    elif event.key == K_SPACE:
        fire_bullet(screen, sp, ship2, bullets, -1)
    elif event.key == K_w:
        ship1.movingup = True
    elif event.key == K_UP:
        ship2.movingup = True
    elif event.key == K_s:
        ship1.movingdown = True
    elif event.key == K_DOWN:
        ship2.movingdown = True

def check_events(ship1, ship2, bullets, screen, sp):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            check_keydown_event(event, ship1, ship2, bullets, screen, sp)
        elif event.type == KEYUP:
            check_keyup_event(event, ship1, ship2)

def check_dead(player1, player2, screen):
    if player2.hp <= 0 or player1.hp <= 0:
        if  player2.hp <=0:
            text = Text(screen, "Player 1 Win!!!")
        else:
            text = Text(screen, "Player 2 Win!!!")
        text.blitme()
        return text
    else:
        return None



def fire_bullet(screen, sp, ship, bullets, special):
    new_bullet = bullet(screen, sp, ship)
    if special == -1:
        new_bullet.speed = -2
    bullets.add(new_bullet)

def bullet_inside(bullet, player):
    if (bullet.rect.centerx < player.rect.right and bullet.rect.centerx > player.rect.left + 150) and (bullet.rect.centery > player.rect.top + 80 and bullet.rect.centery < player.rect.bottom - 80):
        return True
    else:
        return False


def update_bullet(bullets, player1, player2):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left > player1.screen_rect.right or bullet.rect.right < player1.screen_rect.left:
            bullets.remove(bullet)
        if bullet_inside(bullet, player1) and bullet.ship != player1:
            player1.hp -=1
            bullets.remove(bullet)
            print("player1 damaged")
        elif bullet_inside(bullet, player2) and bullet.ship != player2:
            player2.hp -=1
            bullets.remove(bullet)
            print("player2 damaged")

def update_screen(settings, screen, plane1, plane2, bullets, text):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    plane1.blitme()
    plane2.blitme()
    if text != None:
        text.blitme()
    pygame.display.flip()
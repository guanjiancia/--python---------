import sys
import pygame
from bullet import Bullet

def check_games(ship,screen,f_settings,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_down_update(event,ship,screen,f_settings,bullets)
        elif event.type == pygame.KEYUP:
            check_up_update(event,ship)

def check_update(screen,f_settings,ship,bullets,alien):
    screen.fill(f_settings.bg_color)
    ship.blitme()
    alien.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.update(f_settings)
    pygame.display.flip()

def check_down_update(event,ship,screen,f_settings,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
        if len(bullets) < f_settings.bullet_number:
            new_bullet = Bullet(screen,f_settings,ship)
            bullets.add(new_bullet)
    if event.key == pygame.K_q:
        sys.exit()

def check_up_update(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
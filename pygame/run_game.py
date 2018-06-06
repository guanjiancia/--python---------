import sys
import pygame
from settings import Settings
import game_functions as gf
from ship import Ships
from pygame.sprite import Group
from alien import Alien

def run_game():
    pygame.init()
    f_settings = Settings()
    screen = pygame.display.set_mode((f_settings.screen_width,f_settings.screen_height))
    pygame.display.set_caption("外星人")
    bg_color = (f_settings.bg_color)
    ship = Ships(screen)
    bullets = Group()
    alien = Alien(screen,f_settings)
    while True:
        gf.check_games(ship,screen,f_settings,bullets)
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.y < 0:
                bullets.remove(bullet)
        gf.check_update(screen,f_settings,ship,bullets,alien)
run_game()
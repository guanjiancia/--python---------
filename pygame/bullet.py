import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,f_settings,ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,f_settings.bullet_width,f_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.bullet_color = f_settings.bullet_color
        self.bullet_speed = f_settings.bullet_speed
    def update(self):
        self.y -= self.bullet_speed
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.bullet_color,self.rect)
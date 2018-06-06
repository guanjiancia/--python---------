import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,screen,f_settings):
        super().__init__()
        self.screen = screen
        self.alien_image = pygame.image.load("images/alien.png")
        self.screen_rect = screen.get_rect()
        self.rect = self.alien_image.get_rect()
        self.rect.left = self.screen_rect.left
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.alien_image,self.rect)

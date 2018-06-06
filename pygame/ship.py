import pygame

class Ships():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.center = float(self.rect.centerx)
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.bottom = float(self.rect.bottom)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self,f_settings):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += f_settings.speed_spxil
        if self.moving_left and self.rect.left > 0 :
            self.center -= f_settings.speed_spxil
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= f_settings.speed_spxil
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += f_settings.speed_spxil
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom
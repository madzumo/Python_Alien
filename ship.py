import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """class to manage the ship"""

    def __init__(self, ai_game):
        super().__init__()
        # assign game screen to attribute and get full rectangle size of game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        # call rect to access the ship surface rect attribute to later place the ship
        self.rect = self.image.get_rect()

        self.center_ship()

    def blitme(self):
        """draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ update the ships position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        """center ship on the bottom center of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # movement flag. start with a stationary ship
        self.moving_right = False
        self.moving_left = False

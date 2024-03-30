import pygame


class Ship:
    """class to manage the ship"""

    def __init__(self, ai_game):
        # assign game screen to attribute and get full rectangle size of game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        # call rect to access the ship surface rect attribute to later place the ship
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw ship at its current location"""
        self.screen.blit(self.image, self.rect)

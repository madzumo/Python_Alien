import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Main class to manage assets"""

    def __init__(self):
        """Initialize game and set game resources"""
        pygame.init()
        self.s = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.s.screen_width,
                                               self.s.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """main game loop"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """keyboard presses and mouse events"""
        for event in pygame.event.get():  # keyboard & mouse events
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # redraw screen during each pass
        self.screen.fill(self.s.bg_color)
        self.ship.blitme()
        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

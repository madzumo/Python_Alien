class Settings:
    def __init__(self):
        # global settings
        self.debug_app = False
        self.game_title = 'Python Aliens'

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 169 - darker
        self.full_screen_mode = False

        # bullet settings
        self.bullet_speed = 0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4
        self.power_bullet = False

        # alien settings
        self.alien_speed = 0
        self.fleet_drop_speed = 10
        self.fleet_direction = 0  # 1 represents right; -1 represents left
        self.alien_points = 0

        # ship settings
        self.ship_limit = 3
        self.ship_speed = 0

        # scale settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 3
        self.bullet_speed = 5
        self.alien_speed = 2
        self.fleet_direction = 1
        self.alien_points = 25

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)

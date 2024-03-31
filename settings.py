class Settings:
    def __init__(self):
        # global settings
        self.debug_app = False
        self.game_title = 'Python Aliens'

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # 169 - darker
        self.ship_speed = 3
        self.full_screen_mode = False

        # bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

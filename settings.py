class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialze the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3
        self.ship_speed_factor = 5

        self.bullet_width = 600
        self.bullet_height = 300
        self.bullet_color = (60, 60, 60)
        self.bullet_speed_factor = 100
        self.bullets_allowed = 100

        self.fleet_drop_speed = 5

        self.speedup_scale = 1.1
        self.score_scale = 150

        self.initialize_dynamic_settings()

        self.fleet_direction = 1
        self.alien_speed_factor = 5
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        self.alien_points = 10

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings.""" # Screen settings
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3
        
        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30
        # alien settings
        self.fleet_drop_speed = 10
        # how quickly the game speeds up
        self.speedup_scale = 1.1
        # how quickly the alien points increase
        self.score_scale = 1.5

        self.initialize_dynamic_setting()


    def initialize_dynamic_setting(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1.0
        # direction of 1 represent right, -1 represent left
        self.fleet_direction = 1
        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and aliens point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points *= self.score_scale


        
        
        
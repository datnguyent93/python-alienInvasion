class Settings:
    """A class to store all settings of the game"""

    def __init__(self):
        """Initialize with default values"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (173, 216, 230)
        
        #Shipping ship settings
        self.ship_speed = 5
        
import pygame

class Ship:
    """Shipping ship that do the ship things"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        #load the ship image and get its rect.
        self.image = pygame.image.load("assets/ship.bmp")
        self.rect = self.image.get_rect()
        
        # set start point at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        
        #movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update ship location base on movement flag"""
        # Update the ship's x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Update rect object from self x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
import pygame

class Ship:
    """Shipping ship that do the ship things"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        #load the ship image and get its rect.
        self.image = pygame.image.load("assets/ship.bmp")
        self.rect = self.image.get_rect()
        
        # set start point at the bottom center
        self.rect.midbottom = self.screen_rect.midbottom
        
        #movement flag
        self.moving_right = False
        
    def update(self):
        """Update ship location base on movement flag"""
        if self.moving_right:
            self.rect.x += 1
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
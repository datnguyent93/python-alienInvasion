import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Main class manages game assets and behavious"""

    def __init__(self):
        """Constructor initialize the game and assets"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.sceen_width, self.settings.screen_height))  # default dimension is 1200 x 800 (#whoneeds4k)
        pygame.display.set_caption("Alien Invasion")    
        pygame.display.set_caption("by DAT NGUYEN")
        
        #Set background color
        self.bg_color = (230, 230, 230)
        
        
    def run_game(self):
        """Main loop of the game"""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
                    
            #Make the most recently drawn screen visible
            pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, then run it
    ai = AlienInvasion()
    ai.run_game()
    
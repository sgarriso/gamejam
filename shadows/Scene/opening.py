import asyncio
import pygame
import random

class Open:
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    # define the RGB value for white,
    #  green, blue colour .
    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    def __init__(self, display:pygame.display=pygame.display):
        self.screen = display.set_mode((Open.SCREEN_WIDTH, Open.SCREEN_HEIGHT))
        self.display = display
        self.display.set_caption("Start the Game")
        self.clock =  pygame.time.Clock()
        self.running = False
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render('Press A for Alchemy ', True, Open.blue, Open.black)
        self.textRect = self.text.get_rect()
        
        # set the center of the rectangular object.
        self.textRect.center = (Open.SCREEN_WIDTH // 2, Open.SCREEN_HEIGHT // 2)
    async def start(self):
        self.running = True
        while self.running:
            self.screen.fill(Open.black)
            self.screen.blit(self.text, self.textRect)
            for event in pygame.event.get():
 
                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        return
        
            # Draws the surface object to the screen.
            pygame.display.update()
            await asyncio.sleep(0)
            
        
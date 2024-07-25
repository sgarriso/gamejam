import asyncio
import pygame

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
        self.screen.fill(Open.black)
        self.screen.blit(self.text, self.textRect)
        self.event_type = pygame.KEYDOWN
        self.event_key = pygame.K_a
        self.running = True
    def check(self, events):
        self.running = True
        for event in events:
            if event.type == pygame.KEYDOWN and  event.key == pygame.K_a:
                self.running = False
                return False
        return True

            
        
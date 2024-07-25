import asyncio
import pygame
from helper.TextInputBox import TextInputBox



class Main:
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    # define the RGB value for white,
    #  green, blue colour .
    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    def __init__(self, display:pygame.display=pygame.display):
        self.clock = pygame.time.Clock() 
        self.display = display
        
        # it will display on screen 
        self.screen = display.set_mode([600, 500]) 
       # self.manager = pygame_gui.UIManager((600, 500))
        
        # basic font for user typed 
        self.base_font = pygame.font.Font(None, 32) 

        self.text_input_box = TextInputBox(50, 50, 400, self.base_font)
        self.running = False
        self.group = pygame.sprite.Group(self.text_input_box)
        # self.text_input = UITextEntryLine(relative_rect=pygame.Rect(0, 0, 100, 100), manager=self.manager)
    def check(self, events):
        self.running = True
        self.group.update(events)
        self.screen.fill((0))
        self.group.draw(self.screen)
        return True

import pygame
import pygame_gui
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, green



class Main:
    # define the RGB value for white,
    #  green, blue colour .

    def __init__(self, display:pygame.display=pygame.display):
        self.clock = pygame.time.Clock() 
        self.display = display
        
        # it will display on screen 
        self.screen = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.hello = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Ball',
                                             manager=self.manager)
        
        # basic font for user typed 
        self.base_font = pygame.font.Font("freesansbold.ttf", 32) 

        self.text_input =  UITextEntryLine(relative_rect=pygame.Rect(0, 0, 100, 100), manager=self.manager)
        self.running = True
    def check(self, events):
        time_delta = self.clock.tick(60)/1000.0
        self.running = True
        self.screen.fill(green)
        for event in  events:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == self.hello:
                  self.running = False
                  return ["main", "ball"]
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == self.text_input:
                        entered_text = event.text
                        self.text_input.text = entered_text
            self.manager.process_events(event)
        self.manager.update(time_delta)
        self.manager.draw_ui(self.screen)
        return True
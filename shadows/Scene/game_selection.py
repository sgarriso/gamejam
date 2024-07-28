
import pygame
import pygame_gui
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, black
class GameSelect:
    def __init__(self, display:pygame.display=pygame.display):
        self.clock = pygame.time.Clock() 
        self.display = display
        
        # it will display on screen 
        self.screen = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 
        self.manager =  pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.ball = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 2, 0), (100, 50)),
                                             text='Ball',
                                             manager=self.manager)
        self.slots = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, SCREEN_HEIGHT // 1.5), (100, 50)),
                                             text='Slots',
                                             manager=self.manager)
        self.tree = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH - 100, SCREEN_HEIGHT // 1.5), (100, 50)),
                                             text='Tree',
                                             manager=self.manager)

        self.wake = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, SCREEN_HEIGHT // 3), (100, 50)),
                                             text='Awakening',
                                             manager=self.manager)
        self.hi = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH - 100, SCREEN_HEIGHT // 3), (100, 50)),
                                             text='Hi/Low',
                                             manager=self.manager)
        self.treasure = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 2,SCREEN_HEIGHT-100), (100, 50)),
                                             text='Treasure',
                                             manager=self.manager)
        self.pet = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 2, SCREEN_HEIGHT// 2), (100, 50)),
                                             text='Pet',
                                             manager=self.manager)
        self.main = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                             text='Alchemy',
                                             manager=self.manager)
        self.running = True
    def check(self, events):
        time_delta = self.clock.tick(60)/1000.0
        self.screen.fill(black)
        self.running = True
        for event in  events:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.ball:
                  self.running = False
                  return ["game","ball"]
                if event.ui_element == self.main:
                  self.running = False
                  return ["main"]
            self.manager.process_events(event)
        self.manager.update(time_delta)
        self.manager.draw_ui(self.screen)
        return True
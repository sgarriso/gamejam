
import pygame
import pygame_gui
from helper.utils import save_object, restore_object
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, black, OFF
class GameSelect:
    GAMES = {
        "ball": 0,
        "treasure": 1000 ,
        "hi":100 ,
        "wake": 50, 
        "tree": 25,
        "slots":5000,
        
    }
    GAMES_LIST = ["ball", "treasure", "hi", "wake", "tree", "slots", "pet" ]
    def save_settings(results):
        game_menu_settings = restore_object("game_menu_settings")
        for key in results:
            if key in GameSelect.GAMES_LIST:
                game_menu_settings[key] = results[key]
        save_object("game_menu_settings", game_menu_settings)
                
    def __init__(self, display:pygame.display=pygame.display):
        self.clock = pygame.time.Clock() 
        self.display = display
        self.get_settings()
        
        # it will display on screen 
        self.screen = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 
        self.manager =  pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.ball = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 2, 0), (100, 50)),
                                             text='Ball',
                                             visible=self.game_menu_settings.get("ball", 0),
                                             manager=self.manager)
        self.slots = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, SCREEN_HEIGHT // 1.5), (100, 50)),
                                             text='Slots',
                                             visible=self.game_menu_settings.get("slots", 0),
                                             manager=self.manager)
        self.tree = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH - 100, SCREEN_HEIGHT // 1.5), (100, 50)),
                                             text='Tree',
                                             visible=self.game_menu_settings.get("tree", 0),
                                             manager=self.manager)

        self.wake = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, SCREEN_HEIGHT // 3), (100, 50)),
                                             text='Awakening',
                                             visible=self.game_menu_settings.get("wake", 0),
                                             manager=self.manager)
        self.hi = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH - 100, SCREEN_HEIGHT // 3), (100, 50)),
                                             text='Hi/Low',
                                             visible=self.game_menu_settings.get("hi", 0),
                                             manager=self.manager)
        self.treasure = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 2,SCREEN_HEIGHT-100), (100, 50)),
                                             text='Treasure',
                                             visible=self.game_menu_settings.get("treasure", 0),
                                             manager=self.manager)
        self.pet = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 2, SCREEN_HEIGHT// 2), (100, 50)),
                                             text='Pet',
                                             visible=self.game_menu_settings.get("pet", 0),
                                             manager=self.manager)
        self.main = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                             text='Alchemy',
                                             manager=self.manager)
        self.store = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH-100, 0), (100, 50)),
                                             text='Store',
                                             manager=self.manager)
        self.running = True
        self.mapping = {"pet": self.pet,
                        "treasure": self.treasure, 
                        "hi": self.hi, 
                        "wake": self.wake, 
                        "tree": self.tree,
                        "slots": self.slots, 
                        "ball": self.ball
                        }
    def get_settings(self):
        self.game_menu_settings =  restore_object("game_menu_settings")
        result  =  self.game_menu_settings if self.game_menu_settings else save_object("game_menu_settings", {})
        self.game_menu_settings = result if result else {}
    def unlock(self, settings):
        pass
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
                if event.ui_element == self.store:
                    self.running = False
                    return ["store"]
            self.manager.process_events(event)
        self.manager.update(time_delta)
        self.manager.draw_ui(self.screen)
        return True
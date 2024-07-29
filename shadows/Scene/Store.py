import pygame
import pygame_gui
from menus.points import Points
from helper.utils import save_object, restore_object
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, black, OFF
from Scene.game_selection import GameSelect
class Store:
    
    def __init__(self, display:pygame.display=pygame.display):
        self.clock = pygame.time.Clock() 
        self.display = display
        self.get_settings()
        self.get_store_items()
        self.manager =  pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        
        # it will display on screen 
        self.screen = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 
        self.manager =  pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.store_list = pygame_gui.elements.UIDropDownMenu(self.text,starting_option=self.text[0], relative_rect=pygame.Rect((SCREEN_WIDTH // 2, 0), (200, 200)), manager=self.manager)
        #self.welcome_text = pygame_gui.elements.UILabel()
        #self.intro_text = pygame_gui.elements.UILabel()
        #self.pet_text = pygame_gui.elements.UILabel()
    
    def get_settings(self):
        self.game_menu_settings =  restore_object("settings")
        result  =  self.game_menu_settings if self.game_menu_settings else save_object("game_menu_settings", {})
        self.game_menu_settings = result if result else {}
    def get_store_items(self):
        self.text = []
        self.game_text = {}
        for game, value in GameSelect.GAMES.items():
            self.text.append(f"{game}: {value} shadow points")
            self.game_text[f"{game}: {value} shadow points"]= game
    def check(self, events):
        for event in events:
            alchemy_points, shadow_points = Points.get_points()
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                pass
                
                
            self.manager.process_events(event)
        self.screen.fill(black)
        self.manager.update(.00001)
        self.manager.draw_ui(self.screen)
        return True
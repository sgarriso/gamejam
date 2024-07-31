import pygame
import pygame_gui
import pygame_gui.elements.ui_button
from menus.points import Points
from helper.utils import save_object, restore_object
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, black, OFF, ON
from Scene.game_selection import GameSelect
from Scene.main_game import Main
class Store:
    welcome_text = 'Hello! Buy Shadow Games; Play Shadow Games to get more Alchemy points'
    pet_text = "Here have this Pet!"
    intro_text = "To Learn more about shadow games click the About Button"
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
        self.store_list = pygame_gui.elements.UIDropDownMenu(self.text,starting_option=self.text[0], relative_rect=pygame.Rect((SCREEN_WIDTH // 2, 0), (200, 100)), manager=self.manager)
        self.welcome_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, SCREEN_HEIGHT // 4), (555, 100)), text=Store.welcome_text, manager=self.manager)
        self.intro_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, SCREEN_HEIGHT // 2), (550, 100)), text=Store.intro_text, manager=self.manager)
        self.pet_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3), (350, 100)), text=Store.pet_text, manager=self.manager, visible=OFF)
        self.exit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                             text='Exit',
                                             manager=self.manager)
        self.pet_flag = self.game_menu_settings.get("pet", 0)
        if self.store_list.options_list[0] == "the Store is empty":
            self.store_list.disable()
            self.pet_text.hide()
    
    def get_settings(self):
        self.game_menu_settings =  restore_object("game_menu_settings")
        result  =  self.game_menu_settings if self.game_menu_settings else save_object("game_menu_settings", {})
        self.game_menu_settings = result if result else {}
    def get_store_items(self):
        self.text = []
        self.game_text = {}
        for game, value in GameSelect.GAMES.items():
            if not self.game_menu_settings.get(game):
                self.text.append(f"{game}: {value} SP")
                self.game_text[f"{game}: {value} SP"] = game
        if len(Main.get_word_count_discover()) >=4 and Main.get_combo() != 1:
            self.text.append(f"combo: 100 SP")
            self.game_text[f"combo: 100 SP"] = "combo"
        if not self.text:
            self.text.append("the Store is empty")
            
            
    def check(self, events):
        results = True
        time_delta = self.clock.tick(60)/1000.0
        
        for event in events:
            alchemy_points, shadow_points = Points.get_points()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.exit:
                    self.running = False
                    return ["game"]
            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if self.game_text.get(event.text, None) == "combo" and 100 <= shadow_points:
                    results = {}
                    self.store_list.remove_options(event.text)
                    results['shadow'] = -1 * 100
                    save_object("combo", 1)
                    
                elif GameSelect.GAMES.get(self.game_text.get(event.text, None), 99999 )  <= shadow_points:
                    self.store_list.remove_options(event.text)
                    results = {}
                    results['shadow'] = -1 * GameSelect.GAMES.get(self.game_text.get(event.text, None), 999999 )
                    if not self.pet_flag:
                        self.pet_flag = 1
                        results["pet"] = 1
                        self.pet_text.show()
                    else:
                        self.pet_text.hide()
                        
                    results[self.game_text[event.text]] = 1
                if event.text == 'the Store is empty':
                    self.store_list.disable()
                    continue
                if len(self.store_list.options_list) == 0:
                    self.store_list.add_options(["the Store is empty"])
                    self.store_list.selected_option = self.store_list.options_list[0]
                    
                self.store_list.selected_option = self.store_list.options_list[0]
                    
                
                
            self.manager.process_events(event)
        self.screen.fill(black)
        self.manager.update(time_delta)
        self.manager.draw_ui(self.screen)
        return results

import pygame
import pygame_gui
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, black, OFF
from helper.utils import save_object, restore_object
from menus.points import Points



class Main:
    WORD_LIST =  ["fire", "water", "air", "earth", "dark", "light", "phoenix", "tomb", "cookies", "book_of_life", "elixir_of_life"]
    TYPE_WORDS = ["fire", "water", "air", "earth"]
    WORD_COST = {
        "fire": 10,
        "water": 100 ,
        "air":200 ,
        "earth": 3000, 
        "dark": 10000,
        "light":5000,
        
    }
    def save_settings(results):
        player_items = restore_object("items")
        for key in results:
            if key in Main.WORD_LIST:
                player_items[key] = results[key]
        save_object("items", player_items)
    def get_items():
            result =  restore_object("items")
            result  =  result if result else save_object("items", {})
            return result if result else {}

    
    def get_word_count_discover():
        result = restore_object("words")
        return result if result else []
    def get_combo():
        result = restore_object("combo")
        return result if result else 0
        
    warning_text = 'NOT ENOUGH POINTS'   

    def __init__(self, display:pygame.display=pygame.display):
        
        self.clock = pygame.time.Clock() 
        self.display = display
        self.items = Main.get_items()

        self.words_discovered:list =  Main.get_word_count_discover()
        # it will display on screen 
        self.screen = display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 
        self.manager =  pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.games = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (200, 50)),
                                             text='Shadow Games',
                                             manager=self.manager)
        self.submit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((SCREEN_WIDTH // 2 + 100, 0), (200, 50)),
                                             text='Summon',
                                             manager=self.manager, visible=OFF)
        self.text_input =  UITextEntryLine(relative_rect=pygame.Rect(SCREEN_WIDTH // 2, 0, 100, 100), manager=self.manager)
        self.combo = Main.get_combo()
        self.text = list(self.items.keys())
        if not self.text:
            self.text = ["no items to select"]
        self.combo_list_1 = pygame_gui.elements.UIDropDownMenu(self.text,starting_option=self.text[0], relative_rect=pygame.Rect((SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2- 150), (200, 100)), manager=self.manager, visible=self.combo)
        self.combo_list_2 = pygame_gui.elements.UIDropDownMenu(self.text,starting_option=self.text[0], relative_rect=pygame.Rect((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 150), (200, 100)), manager=self.manager, visible=self.combo)
        self.combo_list_3 = pygame_gui.elements.UIDropDownMenu(self.text,starting_option=self.text[0], relative_rect=pygame.Rect((SCREEN_WIDTH // 2 - 300 , SCREEN_HEIGHT // 2 - 150), (200, 100)), manager=self.manager, visible=self.combo)
        self.mix = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0 ), (200, 50)),
                                             text='Combine',
                                             manager=self.manager, visible=self.combo)
        self.warning = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, SCREEN_HEIGHT  - 200 ), (200, 100)), text=Main.warning_text, manager=self.manager, visible=OFF)
        if not self.items.keys():
            self.combo_list_1.hide()
            self.combo_list_2.hide()
            self.combo_list_3.hide()
            self.mix.hide()
        self.running = True
        self.check_word = ""
        if len(self.words_discovered) >= 4:
            Main.TYPE_WORDS.append("dark")
            Main.TYPE_WORDS.append("light")
    def update_drop_down(self):
        self.text = list(self.items.keys())
        self.combo_list_1.clear()
        self.combo_list_2.clear()
        self.combo_list_3.clear()
        self.combo_list_1 = pygame_gui.elements.UIDropDownMenu(self.text,starting_option=self.text[0], relative_rect=pygame.Rect((SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2- 150), (200, 100)), manager=self.manager, visible=self.combo)
        self.combo_list_2 = pygame_gui.elements.UIDropDownMenu(self.text,starting_option=self.text[0], relative_rect=pygame.Rect((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 150), (200, 100)), manager=self.manager, visible=self.combo)
        self.combo_list_3 = pygame_gui.elements.UIDropDownMenu(self.text,starting_option=self.text[0], relative_rect=pygame.Rect((SCREEN_WIDTH // 2 - 300 , SCREEN_HEIGHT // 2 - 150), (200, 100)), manager=self.manager, visible=self.combo)
        
    def check(self, events:list[pygame.Event]):
        time_delta = self.clock.tick(60)/1000.0
        results = True
        self.screen.fill(black)
        self.running = True
        for event in  events:
            alchemy_points, shadow_points = Points.get_points()
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == self.games:
                  self.running = False
                  return ["main", "game"]
              elif event.ui_element == self.submit:
                    if Main.WORD_COST[self.check_word] <= alchemy_points:
                        if self.check_word not in self.words_discovered:
                            self.words_discovered.append(self.check_word)
                            save_object("words",self.words_discovered)
                        results = {}
                        results['alchemy'] = -1 * Main.WORD_COST[self.check_word]
                        results['shadow'] = 1 * Main.WORD_COST[self.check_word]
                        self.items[self.check_word] = self.items.get(self.check_word, 0) + 1
                        Main.save_settings(self.items)
                        self.update_drop_down()
                    else:
                        self.warning.show()
                            
                    self.check_word = ""
                    self.submit.set_text('Summon')
                    self.submit.hide()
                    self.text_input.clear()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                    self.warning.hide()
                    if event.ui_element == self.text_input:
                        entered_text = str(event.text)
                        if entered_text.lower() in Main.TYPE_WORDS:
                            self.check_word = entered_text.lower()
                            self.submit.set_text(f"{self.submit.text} ({Main.WORD_COST[self.check_word]})")
                            self.submit.show()
                        else:
                            self.check_word = ""
                            self.submit.hide()
                            
            self.manager.process_events(event)
        self.screen.fill(black)
        self.manager.update(time_delta)
        self.manager.draw_ui(self.screen)
        return results
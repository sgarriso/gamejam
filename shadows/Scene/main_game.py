
import pygame
import pygame_gui
from pygame_gui.elements.ui_text_entry_line import UITextEntryLine
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, black, OFF
from helper.utils import save_object, restore_object



class Main:
    WORD_LIST =  ["fire", "water", "air", "earth", "dark", "light", "phoenix", "tomb", "cookies", "book_of_life", "elixir_of_life"]
    TYPE_WORDS = ["fire", "water", "air", "earth"]
    def save_settings(results):
        player_items = restore_object("items")
        for key in results:
            if key in Main.WORD_LIST:
                player_items[key] = results[key]
        save_object("items", player_items)
    
    def save_unlock_flag(unlock):
        player_items = restore_object("items")
        

    def __init__(self, display:pygame.display=pygame.display):
        self.clock = pygame.time.Clock() 
        self.display = display
        result = restore_object("words")
        result = result if result else []
        self.words_discovered:list = result
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
        self.running = True
        self.check_word = ""
        if len(self.words_discovered) >= 4:
            Main.TYPE_WORDS.append("dark")
            Main.TYPE_WORDS.append("light")
        
    def check(self, events:list[pygame.Event]):
        time_delta = self.clock.tick(60)/1000.0
        self.screen.fill(black)
        self.running = True
        for event in  events:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == self.games:
                  self.running = False
                  return ["main", "game"]
              elif event.ui_element == self.submit:
                    if self.check_word not in self.words_discovered:
                      self.words_discovered.append(self.check_word)
                      save_object("words",self.words_discovered)
                    self.check_word = ""
                    self.submit.hide()
                    self.text_input.clear()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                    if event.ui_element == self.text_input:
                        entered_text = str(event.text)
                        if entered_text.lower() in Main.TYPE_WORDS:
                            self.check_word = entered_text.lower()
                            self.submit.show()
                        else:
                            self.check_word = ""
                            self.submit.hide()
                            
            self.manager.process_events(event)
        self.manager.update(time_delta)
        self.manager.draw_ui(self.screen)
        return True
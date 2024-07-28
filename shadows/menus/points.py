import pygame_gui
import pygame
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, ON, OFF
class Points:

    
    def __init__(self):
        self.clock = pygame.time.Clock() 
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.alchemy_points = 0
        self.shadow_points = 0
        self.alchemy_text =   pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, SCREEN_HEIGHT-200, 200, 200), text=f"alchemy points:{self.alchemy_points}", manager=self.manager, visible=OFF)
        self.shadow_text  =   pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SCREEN_WIDTH-200, SCREEN_HEIGHT-200, 200,  200), text=f"shadow points:{self.shadow_points}", manager=self.manager, visible=OFF)
    def set_alchemy_text(self,points):
        self.alchemy_points = points
        self.alchemy_text.set_text(f"alchemy points:{self.alchemy_points}")
        self.alchemy_text.show()
    
    def set_shadow_text(self,points):
        self.shadow_points = points
        self.shadow_text.set_text(f"shadow points:{self.shadow_points}")
        self.shadow_text.show()
    def update(self, results):
        self.set_alchemy_text(self.alchemy_points + results.get("alchemy", 0))
        if results.get("shadow", 0):
            self.set_shadow_text(self.shadow_points + results.get("shadow", 0))
    
    def check(self, screen):
        time_delta = self.clock.tick(60)/1000.0
        self.manager.update(time_delta)
        self.manager.draw_ui(screen)
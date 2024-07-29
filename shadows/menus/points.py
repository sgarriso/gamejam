import pygame_gui
import pygame
from helper.utils import save_object, restore_object
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, ON, OFF
class Points:
    def get_points()-> tuple[int, int]:
        alchemy_points = restore_object("alchemy_points")
        shadow_points =  restore_object("shadow_points")
        alchemy_points = alchemy_points if alchemy_points else 0
        shadow_points = shadow_points if shadow_points else 0
        return alchemy_points, shadow_points

    
    def __init__(self):
        self.clock = pygame.time.Clock() 
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.get_points_saved()
        self.alchemy_text =   pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, SCREEN_HEIGHT-150, 200, 200), text=f"alchemy points:{self.alchemy_points}", manager=self.manager, visible=OFF)
        self.shadow_text  =   pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SCREEN_WIDTH-200, SCREEN_HEIGHT-150, 200,  200), text=f"shadow points:{self.shadow_points}", manager=self.manager, visible=OFF)
    def set_alchemy_text(self,points):
        self.alchemy_points = points
        self.alchemy_text.set_text(f"alchemy points:{self.alchemy_points}")
        self.alchemy_text.show()
        save_object("alchemy_points", self.alchemy_points)
        
    
    def set_shadow_text(self,points):
        self.shadow_points = points
        self.shadow_text.set_text(f"shadow points:{self.shadow_points}")
        self.shadow_text.show()
        save_object("shadow_points", self.shadow_points)
    def update(self, results):
        if results.get("alchemy", 0):
            self.set_alchemy_text(self.alchemy_points + results.get("alchemy", 0))
        if results.get("shadow", 0):
            self.set_shadow_text(self.shadow_points + results.get("shadow", 0))
    def get_points_saved(self):
        self.alchemy_points =  restore_object("alchemy_points")
        result  =  self.alchemy_points if self.alchemy_points else save_object("alchemy_points", 0)
        self.alchemy_points = result if result else {}
        self.shadow_points =  restore_object("shadow_points")
        result  =  self.shadow_points if self.shadow_points else save_object("shadow_points", 0)
        self.shadow_points= result if result else {}
    
    def check(self, screen):
        time_delta = self.clock.tick(60)/1000.0
        self.manager.update(time_delta)
        self.manager.draw_ui(screen)
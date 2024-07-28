import pygame
import pygame_gui
import random
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, RED

class Ball:
    # Colors
    RED = (255, 0, 0)
    COLORS = [(255, 255, 255), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    # Constants
    CIRCLE_RADIUS = 15
    SPEED = 5
    # Global variables
    circle_x = random.randint(CIRCLE_RADIUS, SCREEN_WIDTH - CIRCLE_RADIUS)
    circle_y = random.randint(CIRCLE_RADIUS, SCREEN_HEIGHT - CIRCLE_RADIUS)
    circle_dx = SPEED
    circle_dy = 0
    circle_color = RED
    
    pygame.display.set_caption("Click the Circle")

    def __init__(self, display:pygame.display=pygame.display, support=.20):
        self.screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = display
        self.display.set_caption("Click the Circle")
        self.clock =  pygame.time.Clock()
        self.running = True
        self.screen.fill((0, 0, 0))
        self.support = float(support)
        self.count = 0
        self.chances = 5
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.safety = False
        
        # basic font for user typed 
        self.base_font = pygame.font.Font("freesansbold.ttf", 32) 

        self.chances_text =   pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, 0, 100, 100), text=f"chances:{self.chances}", manager=self.manager)
        self.count_text =   pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SCREEN_WIDTH-100, 0, 100,  100), text=f"count:{self.count}", manager=self.manager)
        
    def update_support(self, support):
        self.support = support  

    def check(self, events):
        try:
            time_delta = self.clock.tick(60)/1000.0
            self.screen.fill((0, 0, 0))
            # Draw the circle
            pygame.draw.circle(self.screen, Ball.circle_color, (Ball.circle_x, Ball.circle_y), Ball.CIRCLE_RADIUS)

            # Move the circle
            Ball.circle_x += Ball.circle_dx
            Ball.circle_y += Ball.circle_dy

            # Check for wall collision
            if Ball.circle_x - Ball.CIRCLE_RADIUS <= 0 or Ball.circle_x + Ball.CIRCLE_RADIUS >= SCREEN_WIDTH:
                Ball.circle_dx = -Ball.circle_dx
                if not self.safety:
                    self.chances = self.chances - 1
                    self.chances_text.set_text(f"chances:{self.chances}")
                else:
                    self.safety = False
            if not self.chances:
                self.running = False
                return False, self.count * 10

            # Check for events
            for event in  events:
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    distance = (((mouse_x - Ball.circle_x) ** 2 + (mouse_y - Ball.circle_y) ** 2) ** 0.5)
                    if  distance - (distance * self.support) <= Ball.CIRCLE_RADIUS:
                        Ball.circle_dx = -Ball.circle_dx
                        Ball.circle_color = random.choice([c for c in Ball.COLORS if c != Ball.circle_color])
                        self.count = self.count + 1
                        self.count_text.set_text(f"count:{self.count}")
                        self.safety = True
                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)
        except Exception as e:
            print(e)
            self.running  = False
        return True
                


    
    
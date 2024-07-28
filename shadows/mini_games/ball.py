import pygame
import pygame_gui
import random
from helper.constants import SCREEN_HEIGHT, SCREEN_WIDTH, RED, black

class Ball:
    # Colors
    COLORS = [(255, 255, 255), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    # Constants
    CIRCLE_RADIUS = 15
    SPEED = 5
    # Global variables

    
    pygame.display.set_caption("Click the Circle")

    def __init__(self, display:pygame.display=pygame.display, support=.20):
        self.circle_x = random.randint(Ball.CIRCLE_RADIUS + 100, SCREEN_WIDTH - 200  - Ball.CIRCLE_RADIUS)
        self.circle_y = random.randint(Ball.CIRCLE_RADIUS + 100, SCREEN_HEIGHT - 200 - Ball.CIRCLE_RADIUS)
        self.circle_dx = Ball.SPEED
        self.circle_dy = 0
        self.circle_color = RED
        self.screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = display
        self.display.set_caption("Click the Circle")
        self.clock =  pygame.time.Clock()
        self.running = True
        self.screen.fill((0, 0, 0))
        self.support = float(support)
        self.count = 0
        self.chances = 3
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.safety = True
        self.chances_text =   pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, 0, 100, 100), text=f"chances:{self.chances}", manager=self.manager)
        self.count_text =   pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SCREEN_WIDTH-100, 0, 100,  100), text=f"count:{self.count}", manager=self.manager)
        
    def update_support(self, support):
        self.support = support  

    def check(self, events):
        try:
            time_delta = self.clock.tick(60)/1000.0
            self.screen.fill(black)
            # Draw the circle
            pygame.draw.circle(self.screen, self.circle_color, (self.circle_x, self.circle_y), Ball.CIRCLE_RADIUS)

            # Move the circle
            self.circle_x += self.circle_dx
            self.circle_y += self.circle_dy

            # Check for wall collision
            if self.circle_x - self.CIRCLE_RADIUS <= 0 or self.circle_x + Ball.CIRCLE_RADIUS >= SCREEN_WIDTH:
                self.circle_dx = -self.circle_dx
                if not self.safety:
                    self.chances = self.chances - 1
                    self.chances_text.set_text(f"chances:{self.chances}")
                else:
                    self.safety = False
            if not self.chances:
                self.running = False
                return {"alchemy": self.count * 10}

            # Check for events
            for event in  events:
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    distance = (((mouse_x - self.circle_x) ** 2 + (mouse_y - self.circle_y) ** 2) ** 0.5)
                    if  distance - (distance * self.support) <= Ball.CIRCLE_RADIUS:
                        self.circle_dx = -self.circle_dx
                        self.circle_color = random.choice([c for c in Ball.COLORS if c != self.circle_color])
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
                


    
    
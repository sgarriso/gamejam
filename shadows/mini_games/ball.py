import asyncio
import pygame
import random

class Ball:
    # Colors
    RED = (255, 0, 0)
    COLORS = [(255, 255, 255), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    # Constants
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    CIRCLE_RADIUS = 15
    SPEED = 5
    # Global variables
    circle_x = random.randint(CIRCLE_RADIUS, SCREEN_WIDTH - CIRCLE_RADIUS)
    circle_y = random.randint(CIRCLE_RADIUS, SCREEN_HEIGHT - CIRCLE_RADIUS)
    circle_dx = SPEED
    circle_dy = 0
    circle_color = RED
    
    pygame.display.set_caption("Click the Circle")

    def __init__(self, display:pygame.display=pygame.display):
       self.screen = display.set_mode((Ball.SCREEN_WIDTH, Ball.SCREEN_HEIGHT))
       self.display = display
       self.display.set_caption("Click the Circle")
       self.clock =  pygame.time.Clock()
       self.running = False

    async def start_game(self):
        print("starting ball")
        self.running = True
        try:
            while self.running:
                self.screen.fill((0, 0, 0))

                # Draw the circle
                pygame.draw.circle(self.screen, Ball.circle_color, (Ball.circle_x, Ball.circle_y), Ball.CIRCLE_RADIUS)

                # Move the circle
                Ball.circle_x += Ball.circle_dx
                Ball.circle_y += Ball.circle_dy

                # Check for wall collision
                if Ball.circle_x - Ball.CIRCLE_RADIUS <= 0 or Ball.circle_x + Ball.CIRCLE_RADIUS >= Ball.SCREEN_WIDTH:
                    Ball.circle_dx = -Ball.circle_dx

                # Check for events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        distance = ((mouse_x - Ball.circle_x) ** 2 + (mouse_y - Ball.circle_y) ** 2) ** 0.5
                        if distance <= Ball.CIRCLE_RADIUS:
                            Ball.circle_dx = -Ball.circle_dx
                            Ball.circle_color = random.choice([c for c in Ball.COLORS if c != Ball.circle_color])
                self.display.flip()
                await asyncio.sleep(0)  # Let other tasks run
                
        except Exception as e:
            print(e)
            self.running  = False
        return False

    
    
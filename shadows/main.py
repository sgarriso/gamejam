import pygame
import random
import asyncio
from  mini_games.ball import  Ball
from Scene.opening import Open

# Initialize pygame
pygame.init()







clock = pygame.time.Clock()

async def main():
    running = True


    while running:
        open = Open()
        await open.start()
        
        print("getting ball")
        b = Ball()
        print("running ball")
        running =  await b.start_game()
        

# This is the program entry point
asyncio.run(main())
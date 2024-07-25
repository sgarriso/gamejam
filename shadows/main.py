import pygame
import asyncio
from  mini_games.ball import  Ball
from Scene.opening import Open
from Scene.main_game import Main
from collections import deque 


# Initialize pygame
pygame.init()





def check(object, events):
    return object.check(events)
    

clock = pygame.time.Clock()

async def main():
    queue = deque([Main, Open])
    object = queue.pop()()

 


    while queue or object.running:
        await asyncio.sleep(0)
        if not object.running:
            object = queue.pop()()
        
        events = pygame.event.get()
        
        if check(object, events):
            object.display.update()

        


        

# This is the program entry point
asyncio.run(main())
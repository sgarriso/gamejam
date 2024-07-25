import pygame
import asyncio
import pygame_gui
import i18n
from  mini_games.ball import  Ball
from Scene.opening import Open
from Scene.main_game import Main
from collections import deque 


# Initialize pygame
pygame.init()


mapping = {"ball":Ball, "main":Main}


def check(object, events):
    return object.check(events)
def process(results, queue:deque,object):
    if results:
        object.display.update()
    if isinstance(results, list):
        for item in results:
            if item in mapping.keys():
                queue.append(mapping[item])
        
        
        
    

clock = pygame.time.Clock()


async def main():
    display = pygame.display
    queue = deque([Main, Open])
    object = queue.pop()(display)
    display = object.display 

 


    while queue or object.running:
        await asyncio.sleep(0)
        if not object.running:
            object = queue.pop()()
        
        events = pygame.event.get()
        
        results = check(object, events)
        process(results,queue,object)
                

        


        

# This is the program entry point
asyncio.run(main())
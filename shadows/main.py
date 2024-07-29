import pygame
import asyncio
import pygame_gui
import i18n
import json
from  mini_games.ball import  Ball
from Scene.opening import Open
from Scene.main_game import Main
from Scene.Store import Store
from Scene.game_selection import GameSelect
from menus.points import Points
from collections import deque 
from helper.utils import save_object, restore_object

# pygbag --archive gamejam\shadows



# Initialize pygame
pygame.init()
result =  restore_object("support")
result  =  result if result else save_object("support", .20)
support = result if result else .20
points = Points()


mapping = {"ball":Ball, "main":Main, "game":GameSelect, "store": Store}
args = {Ball:{"support": support }, GameSelect: {}}


def check(object, events):
    return object.check(events)
def process(results, queue:deque,object):
    if results:
        points.check(object.screen)
        object.display.update()
       
    if isinstance(results, list):
        for item in results:
            if item in mapping.keys():
                queue.append(mapping[item])
    if isinstance(results, dict):
        points.update(results)
        GameSelect.save_settings(results)
        
        
        
    

clock = pygame.time.Clock()


async def main():
    display = pygame.display
    queue =  deque([Main, Open])
    object = queue.pop()(display)
    display = object.display 

 


    while queue or object.running:
        await asyncio.sleep(0)
        if not object.running:
            object = queue.pop()
            pass_args = args.get(object, {})
            object =  object(display,**pass_args)if args else object(display)
            display = object.display
        
        events = pygame.event.get()
        
        results = check(object, events)
        process(results,queue,object)
                

        


        

# This is the program entry point
asyncio.run(main())
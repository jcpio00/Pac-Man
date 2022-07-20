
import pygame, sys


pygame.init()


class Timer:

    def __init__(self):
        self.counter = 12100
        self.text = str(self.counter//100)
        #self.event = pygame.USEREVENT + 0
        #pygame.time.set_timer(self.event, 1000)
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        
        
    def run_timer(self):
        #for e in pygame.event.get():
            #if e.type == self.event:
        self.counter -= 1
        self.text = str(self.counter//100) if self.counter//100 > 0 else "End"          

            


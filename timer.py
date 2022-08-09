
import pygame
from settings import *


pygame.init()


class Timer:

    def __init__(self):
        #20100
        self.counter = 1000
        self.text = str(self.counter//100)
        self.font = pygame.font.Font(arcade, 30)
        
        
    def run_timer(self):
        if self.counter//100 > 0:
            self.counter -= 1
            self.text = str(self.counter//100)
        else:
            self.text = "TIME'S UP"
                

    def times_up(self):
        return self.text == "TIME'S UP"
    

    def times_up_delay(self):
        event = pygame.USEREVENT 
        pygame.time.set_timer(event, 1000)
        
        delay = 2
        while delay > 0:
            for e in pygame.event.get():
                if e.type == pygame.USEREVENT:
                    delay -= 1

        
    def timer_reset(self):
        self.counter = 20100
        self.text = str(self.counter//100)

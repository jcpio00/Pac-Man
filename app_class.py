
import pygame
from player_class import *
from settings import *

pygame.init()
vec = pygame.math.Vector2

class App:

    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        self.cell_width = maze_width //28
        self.cell_height = maze_height // 30
        self.player = Player(self, player_starting_position)
        pygame.display.flip()


app = App()




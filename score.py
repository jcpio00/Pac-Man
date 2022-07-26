
import pygame, sys

pygame.init()
vec = pygame.math.Vector2


class Score:
    def __init__(self):
        self.score_value = 0
        self.text = str(self.score_value)
        self.font = pygame.font.Font("freesansbold.ttf", 50)

import pygame
from pygame import QUIT,KEYDOWN
import sys
# screen = pygame.display.set_mode((500,480))
# player1 = pygame.image.load('ghost1.png')
# player2 = pygame.image.load('ghost2.png')
# background = pygame.image.load('maze_background.png')
# screen.blit(background, (0, 0))        #draw the background
# objects = []
class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right>640 or self.pos.left==0:
            self.speed=-self.speed
        else:
            self.speed=self.speed

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load('ghost1.bmp').convert()
background = pygame.image.load('maze_background.bmp').convert()
screen.blit(background, (0, 0))
objects = []
for x in range(1,4):                    #create multiple objects </i>
     o = GameObject(player, x*40, x)
     objects.append(o)

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
    for o in objects:
         screen.blit(background, o.pos, o.pos)
    for o in objects:
         o.move()
         screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(100)
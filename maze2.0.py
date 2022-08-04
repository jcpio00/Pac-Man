import pygame
from settings import *



WHITE = (255, 255, 255)
GOLD = (153, 153, 0)


# Nice class to hold a wall rect

walls = []  # List to hold the walls

class Wall(object):
     
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)


# set screen for maze & load image into background

screen = pygame.display.set_mode((width, height)) 
bg_img = pygame.image.load('maze_background.png')
bg_img = pygame.transform.scale(bg_img, (width, height))



# draw grid lines


def drawGrid():
    blockSize = 20
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x * blockSize, y * blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)




    
def draw_maze():   
    # Holds the level layout in a list of strings.
    level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W             WWW            WW",
    "W             WWW            WW",
    "W  WWWWWWWWW  WWW   WWWWWWWW WW",
    "W  WWWWWWWWW  WWW   WWWWWWWW WW",
    "W  WWWWWWWWW  WWW   WWWWWWWW WW",
    "W                            WW",
    "W                            WW",
    "W  WWW   WW  WWWWWWWW W  WW  WW",
    "W        WW     WWW   W      WW",
    "W        WW     WWW   W      WW",
    "WWWWWW   WWWWW  WWW WWW  WWWWWW",
    "W    W   WWWWW      WWW  W   WW",
    "W    W   WW           W  W   WW",
    "W    W   WW           W  W   WW",
    "WWWWWW   WW  WWW  WWW W  WWWWWW",
    "W            WWW  WWW         W",
    "W            W      W         W",
    "WWWWWW  WW   WWWWWWWW  W WWWWWW",
    "W    W  WW             W W    W",
    "W    W  WW             W W    W",
    "W    W  WW             W W    W",
    "WWWWWW  WW  WWWWWWWWW  W WWWWWW",
    "W           WWWWWWWWW         W",
    "W              WWW            W",
    "W  WW          WWW         W  W",
    "W  WW                      W  W",
    "W  WW  WW   WWWWWWWWW   W  W  W",
    "W      WW   WWWWWWWWW   W     W",
    "W   WWWWWW     WWW     WWWWW  W",
    "W                             W",
    "W                             W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall
    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                Wall((x, y))
            x += 20
        y += 20
        x = 0
# Draw the scene    
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, GOLD, wall.rect)

    screen.blit(bg_img, (0, 0))

    
    
    
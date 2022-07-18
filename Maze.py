
import pygame


# initiate game
pygame.init()

# clock
clock = pygame.time.Clock()

# Colors
Black = pygame.Color(0, 0, 0)         # Black
White = pygame.Color(255, 255, 255)   # White
Grey = pygame.Color(128, 128, 128)   # Grey
Red = pygame.Color(255, 0, 0)       # Red

# Set screen
Width = 1200
Height = 800
Display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Pac-Man")
Display.fill(Black)


# Maze Limits
def Limits():
    X = 50
    Y = 50
    Wi = 1100
    He = 700
    pygame.draw.rect(Display, Red, (X, Y, Wi, He), 2)
# Create wall


class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 25, 25)


# List to hold the walls
walls = []


class Maze():
    # Holds the level layout in a list of strings.
    level = [
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "  WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEW",
        "  WEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
        "  WEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
        "  WEWWEEEEEEEWWEEEWWEEEEEEEEWWEEEWWEEEEEEEWWEW",
        "  WEWWEWWWWWEWWEWEWWEWWWWWWEWWEWEWWEWWWWWEWWEW",
        "  WEWWEEEEEEEWWEWEWWEWWWWWWEWWEWEWWEEEEEEEWWEW",
        "  WEWWWWWWWWWWWEWEWWEWWEEWWEWWEWEWWWWWWWWWWWEW",
        "  WEWWWWWWWWWWWEEEWWEWWEEWWEWWEEEWWWWWWWWWWWEW",
        "  WEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
        "  WEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
        "  WEWWEEEEEEEEEEEWWEEWWWWWWEEWWEEEEEEEEEEEWWEW",
        "  WEWWWWWWWWWWWWWWWEEWWWWWWEEWWEEEWWWWWWWWWWEW",
        "  WEWWWWWWWWWWWWWWWEEWWWWWWEEWWEEEWWWWWWWWWWEW",
        "  WEWWEEEEEEEEEEEWWEEWWWWWWEEWWEEEWWEEEEEEWWEW",
        "  WEWWEEEEEEEEEEEWWEEWWWWWWEEWWEEEWWEEEEEEWWEW",
        "  EEWWEEEEEEEEEEEWWEEEEEEEEEEWWEEEWWEEEEEEWWEE",
        "  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "  EEWWEEEEEEEEEWWEEWWEEWWEEWWEEWWEEEEEEEEEWWEE",
        "  WEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
        "  WEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
        "  WEWWEEEEEEEEEWWEEWWEEWWEEWWEEWWEEEEEEEEEWWEW",
        "  WEWWEEEEEEEEEWWEEWWEEWWEEWWEEWWEEEEEEEEEWWEW",
        "  WEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
        "  WEWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEW",
        "  WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEW",
        "  WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]

# Parse the level string above. W = wall, E = exit

    x = y = 50
    for row in level:
        for col in row:
            if col == "W":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x, y, 25, 25)
            x += 25
        y += 25
        x = 0

# Draw the maze
    for wall in walls:
        pygame.draw.rect(Display, Grey, wall.rect)
    pygame.display.flip()
    
State = True
while State:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            State = False

    Maze()
    Limits()

    pygame.display.update()
    clock.tick(30)

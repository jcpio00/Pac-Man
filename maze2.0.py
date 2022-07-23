import pygame
from pygame.locals import *

pygame.init()

# set screen for maze1.png

width, height = 800, 450
window = pygame.display.set_mode((width, height))

# load image into background

bg_img = pygame.image.load('maze1.png')
bg_img = pygame.transform.scale(bg_img, (width, height))


WHITE = (255, 255, 255)

# draw grid lines


def drawGrid():
    blockSize = 30
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x * blockSize, y * blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(window, WHITE, rect, 1)


runing = True
while runing:

    # game on

    window.blit(bg_img, (0, 0))
    drawGrid()

    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()

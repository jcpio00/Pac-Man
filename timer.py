import pygame
import time

pygame.init()

#BACKGROUND
screen = pygame.display.set_mode((1000, 800))

#TIMER
clock = pygame.time.Clock()

counter, text = 120, '120'
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.Font('freesansbold.ttf', 50)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT :
            counter -= 1
            text = str(counter) if counter > 0 else "Game Over"
        if e.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(font.render("Time: " + text, True, (205, 255, 54)), (10, 10))
    pygame.display.flip()
    clock.tick(60)
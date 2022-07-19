import pygame
pygame.init()
vec = pygame.math.Vector2


class Timer:

    def __init__(self):
        self.screen = pygame.display.set_mode((300, 80))
        self.clock = pygame.time.Clock()
        self.counter = 120
        self.text = '120'
        self.userevent = pygame.USEREVENT
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.Font('freesansbold.ttf', 50)
        self.run_timer()

    def run_timer(self):
        running = True
        while running:
            for e in pygame.event.get():
                if e.type == pygame.USEREVENT:
                    self.counter -= 1
                    self.text = str(self.counter) if self.counter > 0 else "End"
                if e.type == pygame.QUIT:
                    running = False

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.font.render("Time: " + self.text, True, (205, 255, 54)), (10, 10))
            pygame.display.flip()
            self.clock.tick(60)


Timer()
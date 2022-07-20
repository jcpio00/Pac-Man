
import pygame, sys
from player_class import *
from settings import *
from timer import *

pygame.init()
vec = pygame.math.Vector2

class App:

    def __init__(self):
        # Initializers
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.state = "start"
        self.clock = pygame.time.Clock()
        
        # Maze cells
        self.cell_width = maze_width //28
        self.cell_height = maze_height // 30

        # Imports
        self.player = Player(self, player_starting_position)
        self.timer = Timer()


    def run(self):
        while self.running:
            if self.state == "start":
                self.start_events()
            elif self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            else:
                self.running = False
            
            self.clock.tick(fps)
            
        pygame.quit()
        sys.exit()


############################ Start Functions ########################### 

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "playing"


############################ Playing Functions###########################
                
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(left)
                if event.key == pygame.K_RIGHT:
                    self.player.move(right)
                if event.key == pygame.K_UP:
                    self.player.move(up)
                if event.key == pygame.K_DOWN:
                    self.player.move(down)


    def playing_update(self):
        self.timer.run_timer()
        self.player.update()
                    

    def playing_draw(self):
        self.screen.fill(black)
        self.draw_grid()
        self.player.draw()
        self.draw_timer()
        pygame.display.update()


########################### Test Functions ###############################

    def draw_grid(self):
        for x in range(width// self.cell_width):
            pygame.draw.line(self.screen, grey, (x * self.cell_width, 0), \
                            (x * self.cell_width, height))
        for x in range(height// self.cell_height):
            pygame.draw.line(self.screen, grey, (0, x * self.cell_height), \
                            (width, x * self.cell_height))

############################ Helper Functions ###########################


    def draw_timer(self):
        self.screen.blit(self.timer.font.render("Time: " + self.timer.text, True, (205, 255, 54)), (10, 10))

    


    

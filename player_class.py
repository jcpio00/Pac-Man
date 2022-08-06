
import pygame
from settings import *
from pygame import mixer

vec = pygame.math.Vector2


class Player:

    def __init__(self, app, pos):

        # Position and movement
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = left
        self.stored_direction = None
        self.last_location = self.get_pix_pos()
        
        # Player Sprite
        self.sprite = Pacman_Sprite()
        self.group = pygame.sprite.Group()
        self.group.add(self.sprite)

        # Sound effects
        self.waka = mixer.Sound(path + "\ogg files\waka waka.ogg")
        
        
########################### Essentials ########################
        
    def update(self):
        self.off_screen_handler()

        self.pix_pos += self.direction
        
        if self.time_to_move():
            if self.stored_direction:
                self.direction = self.stored_direction
        
        # Grid position in reference to pix pos
        # X
        self.grid_pos[0] = (self.pix_pos[0] - top_bottom_buffer \
        + self.app.cell_width//2)//self.app.cell_width + 1
        # Y
        self.grid_pos[1] = (self.pix_pos[1] - top_bottom_buffer \
        + self.app.cell_height//2)//self.app.cell_height + 1

        # Pac-Man sprite
        self.sprite.rect.center = (int(self.pix_pos.x), int(self.pix_pos.y))

        
    def draw(self):
            
        #Pac-Man circle
        """
        pygame.draw.circle(self.app.screen , player_color,
        (int(self.pix_pos.x), int(self.pix_pos.y)), self.app.cell_width//2 -2) # self.app.cell_width//2 -2
        """
        
        # Pac-Man test tracker
        pygame.draw.rect(self.app.screen, red, \
        (self.grid_pos[0] * self.app.cell_width + top_bottom_buffer//2, \
        self.grid_pos[1] * self.app.cell_height + top_bottom_buffer//2, \
        self.app.cell_width, self.app.cell_height), 1)
        

    def get_pix_pos(self):
        return vec((self.grid_pos.x * self.app.cell_width) \
        + top_bottom_buffer//2 + self.app.cell_width//2,
        (self.grid_pos.y * self.app.cell_height) + \
        top_bottom_buffer//2 + self.app.cell_height//2)
    

############################## Movement ##################################    

    def move(self, direction):
        self.stored_direction = direction


    def time_to_move(self):
        # Checks if Pac-Man is in center of cell 
        if int(self.pix_pos.x + top_bottom_buffer//2) % self.app.cell_width == 0:
            self.last_location = self.get_pix_pos()
            
            # If so and direction is pressed then he is allowed to move
            if self.direction == right or self.direction == left or self.direction == still:
                return True

        if int(self.pix_pos.y + top_bottom_buffer//2) % self.app.cell_width == 0:
            self.last_location = self.get_pix_pos()
            
            if self.direction == up or self.direction == down or self.direction == still:
                return True
            

    def off_screen_handler(self):   
        if self.pix_pos[0] < 35:
            self.pix_pos[0] = 575

        if self.pix_pos[0] > 575:
            self.pix_pos[0] = 35
        
        if self.pix_pos[1] < 35:
            self.pix_pos[1] = 635

        if self.pix_pos[1] > 635:
            self.pix_pos[1] = 35


######################### Helper Functions ##############################

    def player_reset(self):
        self.grid_pos = vec(13, 24)
        self.pix_pos = self.get_pix_pos()
        self.stored_direction = None
        self.direction = left

    
########################## Sprites #########################################
        
class Pacman_Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Sprites
        self.image = pygame.image.load(path + "\png files\pacman_standard.png")
        self.rect = self.image.get_rect()


    
    
    













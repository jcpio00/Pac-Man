
from pygame import *
import sys
from player_class import *
from settings import *
from timer import *
from score import * 

pygame.init()
vec = pygame.math.Vector2

class App:

    def __init__(self):
        # Initializers
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.state = "start"
        self.clock = pygame.time.Clock()
        self.start_delayed_played = False

        #Files
        mixer.music.load(path + "\ogg files\Pac-man-theme-remix.ogg")
        mixer.music.play(-1)
        self.bg_img = pygame.image.load(path + "\png files\maze_background.png")
        
        # Maze cells
        self.cell_width = maze_width //28
        self.cell_height = maze_height // 30

        # Imports
        self.player = Player(self, player_starting_pos)
        self.timer = Timer()
        self.score = Score()


############################# Core ##############################

    def run(self):
        while self.running:
            if self.state == "start":
                self.start_events()
                self.start_draw()
            elif self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == "game over":
                self.game_over_events()
                self.game_over_draw()
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
                mixer.music.pause()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.running = False


    def start_draw(self):
        
        if not self.start_delayed_played:
            self.start_delayed_played = True
            pygame.time.delay(850)
        
        self.screen.fill(black)
        self.draw_start_screen()
        pygame.display.update()
        

########################### Playing Functions ###########################
                
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
                if event.key == pygame.K_SPACE:
                    self.play_pause_chime()
                    self.pause()


    def playing_update(self):
        if self.timer.times_up():
            self.timer.times_up_delay()
            self.state = "game over"
        else:
            self.timer.run_timer()
        
        self.player.update()
                    

    def playing_draw(self):
        if self.state == "start":
            self.screen.fill(black)
            pygame.display.update()
            return
        
        # Background
        self.screen.fill(black)
        self.load_background()

        # Helper
        self.draw_grid()

        """TEMP"""
        self.test_collision()

        # Draw Items
        self.player.group.draw(self.screen)
        #self.player.draw()
        self.draw_timer()
        self.draw_score()
        
        # Update
        pygame.display.update()


    def pause(self):
        mixer.music.load(path + "\ogg files\pause_music.ogg")
        mixer.music.play(-1)
        paused = True

        while paused:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                        mixer.music.pause()
                        self.play_pause_chime()

                    elif event.key == pygame.K_q:
                        paused = False
                        self.reset()
            
            self.screen.fill(black)
            self.draw_pause()
            pygame.display.update()
            self.clock.tick(5)
                    

########################## Game Over Functions ##########################

    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.reset()
                if event.key == pygame.K_SPACE:
                    self.reset("playing")
    


    def game_over_draw(self):
        if self.state == "start":
            self.screen.fill(black)
            pygame.display.update()
            return
        
        self.screen.fill(black)
        self.draw_game_over()
        pygame.display.update()



########################### Test Functions ###############################

    def draw_grid(self):
        for x in range(width// self.cell_width):
            pygame.draw.line(self.bg_img, grey, (x * self.cell_width, 0), \
                            (x * self.cell_width, height))
        for y in range(height// self.cell_height):
            pygame.draw.line(self.bg_img, grey, (0, y * self.cell_height),  # (0, y * self.cell_height)
                            (width, y * self.cell_height)) # (width, y * self.cell_height)

############################ Draw Functions ###########################

    def draw_timer(self):
        self.screen.blit(self.timer.font.render("Time: " + self.timer.text, True, white), (25, 5))

    def draw_pause(self):
        self.screen.blit(pygame.font.Font(classic, 50).render("PAUSED", True, white), pause_center)
        self.screen.blit(pygame.font.Font(classic, 25).render("Press  the  spacebar  to  continue", True, white), continue_text)
        self.screen.blit(pygame.font.Font(classic, 25).render("Press  Q  to  quit", True, white), quit_text)
        
    def draw_game_over(self):
        self.screen.blit(pygame.font.Font(classic, 50).render("GAME OVER", True, red), game_over_center)
        self.screen.blit(pygame.font.Font(classic, 25).render("Press  the  spacebar  to  play again", True, white), play_again_text)
        self.screen.blit(pygame.font.Font(classic, 25).render("Press  Q  to  quit", True, white), game_over_quit)


    def draw_start_screen(self):
        self.load_pacman_logo()
        self.screen.blit(pygame.font.Font(classic, 25).render("Push  the  Spacebar  to  Play", True, white), start_text)
        self.screen.blit(pygame.font.Font(classic, 25).render("Press  Q  to  exit", True, white), start_exit_text)
        

    def draw_score(self):
        self.screen.blit(self.score.font.render("Score: " + self.score.text, True, white), (250, 5))


        
############################## Helper Functions ##########################

    def reset(self, state = "start"):
        
        # Player Reset
        self.player.player_reset()

        # Timer Reset
        self.timer.timer_reset()
        
        # State Reset
        self.start_delayed_played = False
        self.state = state

        if self.state == "start":
            mixer.music.load(path + "\ogg files\Pac-man-theme-remix.ogg")
            mixer.music.play(-1)
            

    def play_pause_chime(self):
        chime = mixer.Sound(path + "\ogg files\pause_chime.ogg")
        chime.play()


    def test_collision(self):
        #place = ((125 - top_bottom_buffer + self.cell_width//2)// self.cell_width + 1, (425 - top_bottom_buffer + self.cell_height//2)//self.cell_height + 1)
        obstacle = pygame.Rect(125, 425, 20, 20)
        pygame.draw.rect(self.screen, red, obstacle)

        if self.player.sprite.hitbox.colliderect(obstacle):
            pygame.draw.rect(self.screen, white, self.player.sprite.hitbox, 1)
            #self.player.direction = still

        #if self.player.grid_pos[0] + self.player.direction[0] == place[0] and self.player.grid_pos[1] + self.player.direction[1] == place[1]:
        #    pass

            

############################### Load Functions ###############################
            
    def load_background(self):
        self.bg_img = pygame.transform.scale(self.bg_img, (maze_width, maze_height))
        self.screen.blit(self.bg_img, (width//2 - maze_width//2, height//2 - maze_height//2))


    def load_pacman_logo(self):
        logo = pygame.image.load(path + "\png files\pac-man-logo.png")
        logo = pygame.transform.scale(logo, (400, 125))
        self.screen.blit(logo, (100, 100))
        pac_man_art = pygame.image.load(path + "\png files\pac-man-promotional-art.png")
        pac_man_art = pygame.transform.scale(pac_man_art, (100, 100))
        self.screen.blit(pac_man_art, (500, 125))

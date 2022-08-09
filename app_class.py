
from pygame import *
import sys
from player_class import *
from settings import *
from timer import *
from walls_class import *
from pellets_class import *

"""TOO DO"""
# soft reset for death occurence
# animation
# start chime

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

        ###### Files #####

        # Music
        mixer.music.load(path + "\ogg files\Pac-man-theme-remix.ogg")
        mixer.music.play(-1)

        # Chimes
        self.pause_chime = mixer.Sound(path + "\ogg files\pause_chime.ogg")
        self.game_over_chime = mixer.Sound(path + "\ogg files\game_over_chime.ogg")
        self.game_over_chime_played = False
        
        # Images
        self.bg_img = pygame.image.load(path + "\png files\maze_background.png")
        self.logo = pygame.image.load(path + "\png files\pacman_start_screen.png")
        self.pellet = pygame.image.load(path + "\png files\pellet.png")
        self.super_pellet = pygame.image.load(path + "\png files\super_pellet.png")
        self.lives_image = pygame.image.load(path + "\png files\pacman_standard.png")

        ####################
        
        # Maze cells
        self.cell_width = maze_width //28
        self.cell_height = maze_height // 30

        # Imports
        self.player = Player(self, player_starting_pos)
        self.timer = Timer()

        # Maze
        self.score = 0
        self.last_score = 0
        self.level = 1
        self.walls_list = []
        self.pellets_list = []
        self.pellet_count = 0
        self.pellets_counted = False
        self.generated_walls = False
        self.generated_pellets = False
        self.maze = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "WPPPPPPPPPPPPWWPPPPPPPPPPPPW",
            "WPWWWPWWWWWWPWWPWWWWWWPWWWPW",
            "WSWWWPWWWWWWPWWPWWWWWWPWWWSW",
            "WPWWWPWWWWWWPWWPWWWWWWPWWWPW",
            "WPWWWPWWWWWWPWWPWWWWWWPWWWPW",
            "WPPPPPPPPPPPPPPPPPPPPPPPPPPW",
            "WPWWWPWWPWWWWWWWWWWPWWPWWWPW",
            "WPWWWPWWPWWWWWWWWWWPWWPWWWPW",
            "WPPPPPWWPPPPPWWPPPPPWWPPPPPW",
            "WWWWWPWWWWWW WW WWWWWWPWWWWW",
            "    WPWWWWWW WW WWWWWWPW    ",
            "    WPWW            WWPW    ",
            "    WPWW WWWWWWWWWW WWPW    ",
            "WWWWWPWW W        W WWPWWWWW",
            "     P   W        W   P     ",
            "WWWWWPWW W        W WWPWWWWW",
            "    WPWW WWWWWWWWWW WWPW    ",
            "    WPWW            WWPW    ",
            "    WPWW WWWWWWWWWW WWPW    ",
            "WWWWWPWW WWWWWWWWWW WWPWWWWW",
            "WPPPPPPPPPPPPWWPPPPPPPPPPPPW",
            "WPWWWPWWPWWWPWWPWWWPWWPWWWPW",
            "WPWWWPWWPWWWPWWPWWWPWWPWWWPW",
            "WSPWWPPPPPPPP  PPPPPPPPWWPSW",
            "WWPWWPWWPWWWWWWWWWWPWWPWWPWW",
            "WWPWWPWWPWWWWWWWWWWPWWPWWPWW",
            "WPPPPPWWPPPPPWWPPPPPWWPPPPPW",
            "WPWWWWWWWWWWPWWPWWWWWWWWWWPW",
            "WPPPPPPPPPPPPPPPPPPPPPPPPPPW",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW"
        ]

        
        # TEST
        

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
            elif self.state == "win":
                self.win_events()
                self.win_draw()
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
            pygame.time.delay(820)
        
        self.screen.fill(black)
        self.draw_start_screen()
        pygame.display.update()
        

########################### Playing Functions ###########################
                
    def playing_events(self):
        if not self.generated_walls:
            self.generate_walls(self.maze)
            self.generated_walls = True

        self.collision_detection()
        
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
                    self.pause_chime.play()
                    self.pause()


    def playing_update(self):
        self.game_over_checker()
        
        if self.pellet_count == 0 and self.pellets_counted:
            self.timer.times_up_delay()
            self.state = "win"
            
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
        #self.draw_grid()
        #self.player.draw()

        # Generate
        self.generate_pellets(self.maze)
        
        # Draw Items
        self.player.group.draw(self.screen)
        self.draw_timer()
        self.draw_score()
        self.draw_lives()

        
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
                        self.pause_chime.play()

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

        if self.state == "playing":
            self.game_over_chime.stop()
            return
        
        self.screen.fill(black)
        self.draw_game_over()

        if not self.game_over_chime_played:
            self.game_over_chime.play()
            self.game_over_chime_played = True
            
        pygame.display.update()


############################## Win Functions ###################################
    
    def win_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.reset()
                if event.key == pygame.K_SPACE:
                    self.reset("playing")

    def win_draw(self):
        if self.state == "start":
            self.screen.fill(black)
            pygame.display.update()
            return
        
        self.screen.fill(black)
        self.draw_win()
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
        self.screen.blit(pygame.font.Font(classic, 50).render("GAME OVER!", True, red), game_over_center)
        self.screen.blit(pygame.font.Font(classic, 25).render("Press  the  spacebar  to  play again", True, white), play_again_text)
        self.screen.blit(pygame.font.Font(classic, 25).render("Press  Q  to  quit", True, white), game_over_quit)


    def draw_start_screen(self):
        self.screen.blit(self.logo, (0, 0))
        

    def draw_score(self):
        self.screen.blit(pygame.font.Font(arcade, 30).render("Score: " + str(self.score), True, white), (250, 5))


    def draw_lives(self):
        x = 500

        for i in range(1, self.player.lives+1):
            self.screen.blit(self.lives_image, (x, 5))
            x += 20


    def draw_win(self):
        self.screen.blit(pygame.font.Font(classic, 50).render("YOU  WIN!", True, player_color), game_over_center)
        self.screen.blit(pygame.font.Font(classic, 25).render("Press  the  spacebar  to  play again", True, white), play_again_text)
        self.screen.blit(pygame.font.Font(classic, 25).render("Press  Q  to  quit", True, white), game_over_quit)
        

        
############################## Helper Functions #############################

    def reset(self, state = "start"):
        
        # Player Reset
        self.player.player_reset()

        # Timer Reset
        self.timer.timer_reset()
        
        # State Reset
        self.start_delayed_played = False
        self.state = state

        # Maze Reset
        self.score = 0
        self.last_score = 0
        self.pellet_count = 0
        self.pellets_list.clear()
        self.walls_list.clear()
        self.generated_walls = False
        self.generated_pellets = False
        self.pellets_counted = False

        # Start Music Reset         
        if self.state == "start":
            mixer.music.load(path + "\ogg files\Pac-man-theme-remix.ogg")
            mixer.music.play(-1)

        # Other Reset
        self.game_over_chime_played = False
        
        
    
############################### Load Functions ###############################
            
    def load_background(self):
        self.screen.blit(self.bg_img, (width//2 - maze_width//2, height//2 - maze_height//2))

        
############################# Gameplay Functions ##########################

    def game_over_checker(self):
         
        if self.timer.times_up():
            self.timer.times_up_delay()
            self.state = "game over"
        else:
             self.timer.run_timer()

        if self.player.lives == 0:
            self.state = "game over"

            
        
    def collision_detection(self):

        # Wall Collision
        for wal in self.walls_list:
            if self.player.sprite.rect.colliderect(wal):
                # Uncomment this to see player hitbox
                # pygame.draw.rect(self.screen, white, self.player.sprite.rect, 1)

                if self.player.direction == right:
                    self.player.sprite.rect.right = wal.left
                    self.player.pix_pos = self.player.last_location
                    self.player.direction = still
                    self.player.stored_direction = still
                    break
                if self.player.direction == left:
                    self.player.sprite.rect.left = wal.right
                    self.player.pix_pos = self.player.last_location
                    self.player.direction = still
                    self.player.stored_direction = still
                    break
                if self.player.direction == up:
                    self.player.sprite.rect.top = wal.bottom
                    self.player.pix_pos = self.player.last_location
                    self.player.direction = still
                    self.player.stored_direction = still
                    break
                if self.player.direction == down:
                    self.player.sprite.rect.bottom = wal.top
                    self.player.pix_pos = self.player.last_location
                    self.player.direction = still
                    self.player.stored_direction = still
                    break


        # Pellet and Super Pellet Collision
        # Pellet count and Score updater
        for pel in self.pellets_list:
            if self.player.grid_pos == pel.grid_pos:
                if not pel.value_added:
                    pel.eaten = True
                    self.pellet_count -= 1 
                    self.player.waka.play()
                    self.score += pel.value
                    pel.value_added = True

                    if self.score == self.last_score + 2000:
                        self.player.lives += 1 if self.player.lives < 3 else 0
                        self.last_score += 2000



    def generate_walls(self, maze):
        
        # test coords - (125, 425)
        x = 25
        y = 25
        
        for line in maze:
            for char in line:
                if char == "W":
                    curr_wall = Walls((x, y))
                    self.walls_list.append(curr_wall.wall)

                    # Uncomment this to make invisible walls visible and call in playing_draw   
                    #pygame.draw.rect(self.screen, white, curr_wall.wall)

                if x + 20 <= 575: 
                    x += 20
                else:
                    x = 25

            if y + 20 <= 635:
                y += 20

            else:
                y = 25


    def generate_pellets(self, maze):

        # Initial State
        # Generates and figures out how many pellets there are
        if not self.generated_pellets:
            x = 25
            y = 25
            
            for line in maze:
                for char in line:
                    if char == "P":
                        curr_pell = Pellets((x, y))
                        curr_pell.draw_pellet(self.screen, self.pellet)
                        self.pellets_list.append(curr_pell)
                        self.pellet_count += 1

                    elif char == "S":
                        curr_sup = Super_Pellets((x, y))
                        curr_sup.draw_super_pellet(self.screen, self.super_pellet)
                        self.pellets_list.append(curr_sup)
                        self.pellet_count += 1
                        
                    if x + 20 <= 575: 
                        x += 20
                    else:
                        x = 25

                if y + 20 <= 635:
                    y += 20

                else:
                    y = 25

            self.generated_pellets = True
            self.pellets_counted = True
    
        # Playing State
        else:
            for pell in self.pellets_list:
                if not pell.eaten:
                    if pell.pellet_type() == "pellet":
                        pell.draw_pellet(self.screen, self.pellet)

                    else:
                        pell.draw_super_pellet(self.screen, self.super_pellet)


     





        

        

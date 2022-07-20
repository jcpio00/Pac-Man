
from pygame.math import Vector2 as vec


# screen settings
width, height = 610, 670
fps = 60
top_bottom_buffer = 50
maze_width , maze_height = width - top_bottom_buffer, height - top_bottom_buffer


# color settings
black = (0, 0, 0)
red = (208, 22, 22)
grey = (107, 107, 107)
##white = (255, 255, 255)
player_color = (255,211,67)


# player settings
player_starting_position = vec(13, 15)


# controls
left = vec(-1, 0)
right = vec(1, 0)
up = vec(0, -1)
down = vec(0, 1)


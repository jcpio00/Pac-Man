import random

WORLD_SIZE = 20
BLOCK_SIZE = 32
WIDTH = WORLD_SIZE*BLOCK_SIZE
HEIGHT = WORLD_SIZE*BLOCK_SIZE

SPEED = 2
GHOST_SPEED = 1

# An array containing the world tiles
world = []

ghosts = []

# Your level will contain characters, they map
# to the following images
char_to_image = {
    'g': 'ghost1.png',
    'G': 'ghost2.png',
}

def load_level(number):
    file = "level-%s.txt" % number
    with open(file) as f:
        for line in f:
            row = []
            for block in line:
                row.append(block)
            world.append(row)

def set_random_dir(sprite, speed):
    sprite.dx = random.choice([-speed, speed])
    sprite.dy = random.choice([-speed, speed])

def make_ghost_actors():
    for y, row in enumerate(world):
        for x, block in enumerate(row):
            if block in ['g', 'G']:
                # Make the sprite in the correct position
                g = Actor(char_to_image[block], (x*BLOCK_SIZE, y*BLOCK_SIZE), anchor=('left', 'top'))
                set_random_dir(g, GHOST_SPEED)

                ghosts.append(g)
                # Now we have the ghost sprite we don't need this block
                world[y][x] = None

# draw the ghosts
def draw():
    screen.clear()
    for g in ghosts: g.draw()

# move ghosts
def move_ahead(sprite):
    # Record current pos so we can see if the sprite moved
    oldx, oldy = sprite.x, sprite.y
    # Move ghosts in the x and y direction
    sprite.x += sprite.dx
    sprite.y += sprite.dy

    # Keep sprite on the screen
    def wrap_around(mini, val, maxi):
        if val < mini: return maxi
        elif val > maxi: return mini
        else: return val
    sprite.x = wrap_around(0, sprite.x, WIDTH-BLOCK_SIZE)
    sprite.y = wrap_around(0, sprite.y, HEIGHT-BLOCK_SIZE)

    # Return whether we moved
    return oldx != sprite.x or oldy != sprite.y

def update():
    for g in ghosts:
        if not move_ahead(g):
            set_random_dir(g, GHOST_SPEED)

# Game set up
load_level(1)
make_ghost_actors()
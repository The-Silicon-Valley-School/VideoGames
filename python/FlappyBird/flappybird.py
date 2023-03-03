import pgzrun
import random


# Setup
TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 700

GAP = 130
GRAVITY = 0.1
FLAP = 4.5
SPEED = 3

# Characters
bird = Actor("bird1", (75, 200))
bird.dead = False
bird.vel_y = 0  # Vertical velocity for the bird
bird.score = 0

pipe_top = Actor("top_pipe", anchor=("left", "bottom"), pos=(-100, 0))
pipe_bottom = Actor("bottom_pipe", anchor=("left", "top"), pos=(-100, 0))


def reset_pipes():
    pipe_gap_y = random.randint(250, HEIGHT - 250)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)


def update():
    # Update bird
    update_y = bird.vel_y
    bird.vel_y = bird.vel_y + GRAVITY
    bird.y = bird.y + (update_y + bird.vel_y) / 2
    bird.x = 75
    
    if not bird.dead:
        if bird.vel_y < -3:
            bird.image = "bird2"
        else:
            bird.image = "bird1"
    
    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = "birddead"
    
    if bird.y < 0 or bird.y > 720:
        bird.y = 200
        bird.dead = False
        bird.score = 0
        bird.vel_y = 0
        reset_pipes()
    
    
    # Update pipes
    pipe_top.left = pipe_top.left - SPEED
    pipe_bottom.left = pipe_bottom.left - SPEED
    if pipe_top.right < 0:
        reset_pipes()
        bird.score += 1 
    

def on_key_down():
    if not bird.dead:
        bird.vel_y = FLAP * -1
    

def draw():
    screen.blit("background", (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()
    screen.draw.text(
        str(bird.score),
        color="WHITE",
        midtop=(WIDTH // 2, 10),
        fontsize=70,
        shadow=(1,1)
        )
    

pgzrun.go()
import pgzrun


TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 700

GRAVITY = 0.1
FLAP = 6.5

bird = Actor("bird1", (75, 200))
bird.vel_y = 0

def update():
    update_y = bird.vel_y
    bird.vel_y = bird.vel_y + GRAVITY
    bird.y = bird.y + (update_y + bird.vel_y) / 2
    

def on_key_down():
    print(bird.y)
    bird.vel_y = FLAP * -1
    

def draw():
    screen.blit("background", (0, 0))
    bird.draw()
    
    

pgzrun.go()
from pico2d import *
import random

# fill here
TUK_WIDTH,TUK_HEIGHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)

TUK_ground=load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow=load_image('hand_arrow.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running=False


running = True
x,y=TUK_WIDTH//2,TUK_HEIGHT//2
cx,cy=TUK_WIDTH//2,TUK_HEIGHT//2
hx,hy= random.randint(200,700), random.randint(200,700)
p=0
frame=0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    hand_arrow.draw(hx,hy)

    if(cx<hx):
        character.clip_draw(frame*100,100*1,100,100,x,y)
    else:
        character.clip_draw(frame*100,0,100,100,x,y)

    update_canvas()
    frame=(frame+1)%8
    x=(1-p)*cx+p*hx
    y=(1-p)*cy+p*hy
    p+=0.05
    if(p>1.0):
        cx=x
        cy=y
        hx=random.randint(100,1200)
        hy=random.randint(100,1000)
        p=0
    delay(0.05)
    handle_events()

close_canvas()





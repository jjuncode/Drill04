from pico2d import *

open_canvas(736,521)
background = load_image('TUK_GROUND.png')
character = load_image('sprite.png')

center = get_canvas_width()/2,get_canvas_height()/2 # window center

x,y = 400,center[1]   # character pos
move_speed = 15
quit = False

class Ani:
    offset_x = 74       # ani offset x
    offset_y = 80       # ani offset y 
    cur_frame =0
    max_frame = [9,9,9,9,2,0,2,2]    # sprite max frame 
    cur_ani = 0         # cur ani ( from img_bottom )

class Dir:
    x,y = 0,0

def DrawAnimation():
    global x,y
    clear_canvas()
    background.draw(center[0],center[1])
    MoveCharacter()
    character.clip_draw(Ani.cur_frame*Ani.offset_x,Ani.cur_ani*Ani.offset_y,Ani.offset_x,Ani.offset_y
                        ,x,y)
    update_canvas()
 
def SetFrame():
    Ani.cur_frame += 1
    if Dir.x == 0 and Dir.y == 0: # standing motion
        Ani.cur_ani = 7
    if (Ani.cur_frame > Ani.max_frame[Ani.cur_ani]):    # Frame reset
        Ani.cur_frame =0

    delay(0.1)

def MoveCharacter():
    global x,y,move_speed

    x += Dir.x * move_speed
    y += Dir.y * move_speed
    if ( x > 2*center[0] ) : x = 2*center[0]
    if ( y> 2*center[1] ) : y= 2*center[1]
    if ( x < 0 ) : x = 0
    if (y <0 ) : y= 0


def handle_event():
    global quit,dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit = True
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                quit=True
            elif event.key ==SDLK_UP:
                Ani.cur_ani = 1
                Dir.y +=1
            elif event.key == SDLK_DOWN:
                Ani.cur_ani = 3
                Dir.y -=1
            elif event.key == SDLK_LEFT:
                Ani.cur_ani = 2
                Dir.x -=1
            elif event.key == SDLK_RIGHT:
                Ani.cur_ani = 0
                Dir.x +=1
        if event.type == SDL_KEYUP:
            if event.key ==SDLK_UP:
                Dir.y -=1
            elif event.key == SDLK_DOWN:
                Dir.y +=1
            elif event.key == SDLK_LEFT:
                Dir.x +=1
            elif event.key == SDLK_RIGHT:
                Dir.x -=1

while (not quit):
    SetFrame()
    handle_event()
    DrawAnimation()

close_canvas()
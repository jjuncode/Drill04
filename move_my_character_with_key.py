from pico2d import *
import pico2d as pico

open_canvas(736,521)
background = load_image('TUK_GROUND.png')
character = load_image('sprite.png')

center = get_canvas_width()/2,get_canvas_height()/2 # window center

x,y = 400,center[1]   # character pos
move_speed = 50
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

    if (Ani.cur_frame > Ani.max_frame[Ani.cur_ani]):    # Frame reset
        Ani.cur_frame =0

    delay(0.1)

def MoveCharacter():
    global x,y
    x += Dir.x * move_speed;
    y += Dir.y * move_speed;

def handle_event():
    global quit,dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            quit = True
        if event.type == SDL_KEYDOWN:
            if event.key ==SDLK_UP:
                Dir.y +=1
            elif event.key == SDLK_DOWN:
                Dir.y -=1
            elif event.key == SDLK_LEFT:
                Dir.x -=1
            elif event.key == SDLK_RIGHT:
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
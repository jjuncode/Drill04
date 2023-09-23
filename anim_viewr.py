from pico2d import *
import pico2d as pico

open_canvas(736,521)
background = load_image('image_background.png')
character = load_image('sprite.png')

center = get_canvas_width()/2,get_canvas_height()/2 # window 중심점
x,y = 0,center[1]   # character pos
offset_x = 74       # ani offset x
offset_y = 80       # ani offset y 
frame =0            # cur ani frame
cur_ani = 0         # cur ani 

def MoveRight():
    global x,y
    clear_canvas()
    background.draw(center[0], center[1])
    character.clip_draw(frame*offset_x,0,offset_x,offset_y
                        ,x,y)
    update_canvas()
    x += 5
    delay(0.05)

def SetFrame():
    global frame
    frame += 1
    if (frame > 8):
        frame =0

while (1):
    SetFrame()
    MoveRight()
    get_events()
close_canvas()
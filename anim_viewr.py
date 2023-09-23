from pico2d import *
import pico2d as pico

open_canvas(736,521)
background = load_image('image_background.png')
character = load_image('sprite.png')

center = get_canvas_width()/2,get_canvas_height()/2
x,y = 0,center[1]
offset_x = 74
offset_y = 80
frame =0
cur_ani = 0

def MoveRight():
    clear_canvas()
    background.draw(center[0], center[1])
    character.clip_draw(frame*offset_x,cur_ani*offset_y,offset_x,offset_y
                        ,x,y)
    update_canvas()
    delay(0.05)


while (1):
    frame += 1 
    if ( frame > 8):
        frame =0
    MoveRight()
    x += 5
    get_events()
close_canvas()
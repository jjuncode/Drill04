from pico2d import *
import pico2d as pico

open_canvas()
grass = load_image('grass.png')
character = load_image('sprite.png')

x,y = 400,300
offset_x = 74
offset_y = 93
frame =0

def MoveRight():
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*offset_x,frame,offset_x,offset_y,x,y)
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
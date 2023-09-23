from pico2d import *
import pico2d as pico

open_canvas(736,521)
background = load_image('image_background.png')
character = load_image('sprite.png')

center = get_canvas_width()/2,get_canvas_height()/2 # window center

x,y = 0,center[1]   # character pos

class Ani:
    offset_x = 74       # ani offset x
    offset_y = 80       # ani offset y 
    cur_frame =0
    max_frame = [8,8,8,8,3,1,3,3]    # sprite max frame 
    cur_ani = 0         # cur ani ( from img_bottom )

class Distance:
    distn =0

def MoveCharacter():
    global x,y
    clear_canvas()
    background.draw(center[0], center[1])
    character.clip_draw(Ani.cur_frame*Ani.offset_x,Ani.cur_ani*Ani.offset_y,Ani.offset_x,Ani.offset_y
                        ,x,y)
    update_canvas()
    x += 5
 
def SetFrame():
    Ani.cur_frame += 1
    if (Ani.cur_frame >= Ani.max_frame[Ani.cur_ani]):
        Ani.cur_frame =0

    Distance.distn +=5
    if ( Distance.distn > 100 ):
        Ani.cur_ani +=1
        Distance.distn =0
    if ( Ani.cur_ani > 8) : Ani.cur_ani = 0
    delay(0.1)

while (1):
    SetFrame()
    MoveCharacter()
    get_events()
close_canvas()
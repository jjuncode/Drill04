from pico2d import *
import pico2d as pico

open_canvas(736,521)
background = load_image('TUK_GROUND.png')
character = load_image('sprite.png')

center = get_canvas_width()/2,get_canvas_height()/2 # window center

x,y = 400,center[1]   # character pos

class Ani:
    offset_x = 74       # ani offset x
    offset_y = 80       # ani offset y 
    cur_frame =0
    max_frame = [9,9,9,9,2,0,2,2]    # sprite max frame 
    cur_ani = 0         # cur ani ( from img_bottom )

    def FrameReset():
        Ani.cur_frame =0

def DrawAnimation():
    global x,y
    clear_canvas()
    background.draw(x,y,)
    character.clip_draw(Ani.cur_frame*Ani.offset_x,Ani.cur_ani*Ani.offset_y,Ani.offset_x,Ani.offset_y
                        ,x,y)
    update_canvas()
 
def SetFrame():
    Ani.cur_frame += 1

    if (Ani.cur_frame > Ani.max_frame[Ani.cur_ani]):    # Frame reset
        Ani.FrameReset()

    delay(0.1)

def handle_event():
    pass

while (1):
    SetFrame()
    DrawAnimation()
    get_events()
    
close_canvas()
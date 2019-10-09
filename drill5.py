from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
   global running
   global x, y
   global move
   global mouse_x, mouse_y
   global pre_x, pre_y

   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type == SDL_MOUSEMOTION:
           x, y =  event.x, KPU_HEIGHT - 1 - event.y
       elif event.type == SDL_MOUSEBUTTONDOWN:
           move = True
           mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
           pre_x = ch_x
           pre_y = ch_y
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           running = False


def draw():
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    global move
    global ch_dir
    global ch_x
    global ch_y
    global frame

    if move == True:
        if ch_dir == True:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, ch_x, ch_y)
        else:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, ch_x, ch_y)
    else:
        if ch_dir == True:
            character.clip_draw(frame * 100, 100 * 3, 100, 100, ch_x, ch_y)
        else:
            character.clip_draw(frame * 100, 100 * 2, 100, 100, ch_x, ch_y)

    hand_arrow.draw(x, y, 50, 50)

def update_character_position():
    global move
    global mouse_x, mouse_y
    global pre_x, pre_y
    global ch_x, ch_y
    global t
    if move == True:
            t = t + 0.01
            ch_x = (1 - t) * pre_x + t * mouse_x
            ch_y = (1 - t) * pre_y + t * mouse_y
            if t > 1:
                move = False
                t = 0
                



open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
ch_x, ch_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
move = False
ch_dir = True   #true면 오른쪽 false면 왼쪽
t = 0.0
mouse_x = 0
mouse_y = 0
pre_x = 0
pre_y = 0
hide_cursor()

while running:
    clear_canvas()
    #kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, ch_x, ch_y)
    #hand_arrow.draw(x, y, 50, 50)
    draw()
    update_canvas()
    frame = (frame + 1) % 8
    update_character_position()
    handle_events()

close_canvas()





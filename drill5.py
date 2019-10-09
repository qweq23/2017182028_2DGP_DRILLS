from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
   global running
   global x, y
   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type == SDL_MOUSEMOTION:
           x, y =  event.x, KPU_HEIGHT - 1 - event.y
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



hide_cursor()

while running:
    clear_canvas()
    #kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, ch_x, ch_y)
    #hand_arrow.draw(x, y, 50, 50)
    draw()
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()





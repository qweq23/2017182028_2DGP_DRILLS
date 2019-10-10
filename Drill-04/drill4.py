from pico2d import *


def handle_events():
    # fill here
    global running
    global dir
    global  ch_dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                ch_dir = True
            elif event.key == SDLK_LEFT:
                dir += 1
                ch_dir = False
    pass


def draw():
    global dir
    global ch_dir
    grass.draw(400, 30)

    if dir == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    elif dir == -1:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, 90)
    else:
        if ch_dir == False:
            character.clip_draw(100, 100 * 2, 100, 100, x, 90)
        elif ch_dir == True:
            character.clip_draw(100, 100 * 3, 100, 100, x, 90)


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0
ch_dir = True
while running:
    clear_canvas()
    #grass.draw(400, 30)
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, x, 90)
    draw()
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    #delay(0.01)

close_canvas()


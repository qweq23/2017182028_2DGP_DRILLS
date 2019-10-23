import game_framework
from pico2d import *

import main_state

# 이미지가 깜빡이는건 frame 변수 주면 되고,
# 멈춘 이미지를 불러오는 건....

name = "PauseState"
image = None
frame = 0

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del (image)


def update():
    global frame
    frame = (frame + 1) % 200
    handle_events()


def draw():
    global image
    clear_canvas()
    main_state.boy.draw()
    main_state.grass.draw()
    if frame < 100:
        image.draw(400, 300, 100, 100)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            game_framework.pop_state()
            pass

def pause(): pass
def resume(): pass

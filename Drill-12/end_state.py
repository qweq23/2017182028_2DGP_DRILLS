from pico2d import *
import game_framework

font = None


def enter():
    global font
    font = load_font('ENCR10B.TTF', 30)
    print('game over')


def exit():
    pass


def update():
    pass


def draw():
    clear_canvas()
    font.draw(get_canvas_width() / 2 - 100, get_canvas_height() / 2, 'Game Over', (0, 0, 0))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def pause():
    pass


def resume():
    pass

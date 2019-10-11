from pico2d import *
import random as r


def handle_events():
   global running

   events = get_events()
   for event in events:
       if event.type == SDL_QUIT:
           running = False
       elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           running = False


def draw():
    global frame
    global ch_x, ch_y
    global look_right

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if look_right == True:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, ch_x, ch_y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, ch_x, ch_y)


def update_character_position(p1, p2, p3, p4, i):
    global points
    global ch_x, ch_y
    global look_right

    t = i / 100
    x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] +
          (-3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
    y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] +
          (-3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
    if ch_x < x:
        look_right = True
    else:
        look_right = False

    ch_x = x
    ch_y = y

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0
look_right = True
size = 10
points = [(r.randint(0, 1280), r.randint(0, 1024)) for i in range(size)]
n = 1
ch_x, ch_y = points[n - 1]
i = 0

while running == True:
    clear_canvas()
    draw()
    update_canvas()
    frame = (frame + 1) % 8
    update_character_position(points[n - 3], points[n - 2], points[n - 1], points[n], i)
    i = (i + 2) % 100
    if i == 0:
        n = (n + 1) % size
    handle_events()

    delay(0.03)

close_canvas()



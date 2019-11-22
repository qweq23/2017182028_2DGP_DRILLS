import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SPEED_KMPH = 30.0  # Km / Hour
SPEED_MPM = (SPEED_KMPH * 1000.0 / 60.0)
SPEED_MPS = (SPEED_MPM / 60.0)
SPEED_PPS = (SPEED_MPS * PIXEL_PER_METER)


class SmallBall:
    image = None

    def __init__(self):
        if SmallBall.image == None:
            SmallBall.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(10, get_canvas_width() - 10), random.randint(10, get_canvas_height() - 10)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass


class BigBall:
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(20, get_canvas_width() - 20), random.randint(20, get_canvas_height() - 20)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

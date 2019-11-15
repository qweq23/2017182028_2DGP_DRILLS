import game_framework
from pico2d import *

import game_world


# 10 pixel - 30cm
PIXEL_PER_METER = (10.0 / 0.3)

FLY_SPEED_KMPH = 10.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Brick:
    def __init__(self):
        self.x, self.y = 150, 200
        self.image = load_image('brick180x40.png')
        self.velocity = FLY_SPEED_PPS

    def get_bb(self):
        return self.x - 90, self.y + 20, self.x + 90, self.y + 20

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(150, self.x, 1600 - 150)
        if self.x == 1600 - 150:
            self.velocity = -FLY_SPEED_PPS
        if self.x == 150:
            self.velocity = FLY_SPEED_PPS


    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

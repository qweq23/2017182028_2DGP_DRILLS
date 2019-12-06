import random
from pico2d import *
import game_world
import game_framework


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1800-1), random.randint(0, 1100-1)
        self.cx, self.cy = 0, 0
        self.bg = None

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        cx, cy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(cx, cy)
        # draw_rectangle(*self.get_bb())

    def set_background(self, bg):
        self.bg = bg

    def update(self):
        pass


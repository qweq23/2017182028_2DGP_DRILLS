from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
ATTACK_SPEED_KMPH = 40.0  # Km / Hour
ATTACK_SPEED_MPM = (ATTACK_SPEED_KMPH * 1000.0 / 60.0)
ATTACK_SPEED_MPS = (ATTACK_SPEED_MPM / 60.0)
ATTACK_SPEED_PPS = (ATTACK_SPEED_MPS * PIXEL_PER_METER)

class BoyAttack:
    def __init__(self, x, y, dir):
        self.x, self.y, self.dir = x, y, dir
        self.timer = 1.0

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        draw_rectangle(*self.get_bb())

    def update(self):
        self.timer -= game_framework.frame_time
        if self.dir > 0:
            self.x += ATTACK_SPEED_PPS * game_framework.frame_time
        else:
            self.x -= ATTACK_SPEED_PPS * game_framework.frame_time

        if self.timer < 0:
            game_world.remove_object(self)
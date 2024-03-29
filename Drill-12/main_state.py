import random
import json
import os

from pico2d import *
import game_framework
import game_world
import end_state

from boy import Boy
from ground import Ground
from zombie import Zombie
from ball import BigBall
from ball import SmallBall
from boy_attack import BoyAttack

name = "MainState"

boy = None
zombie = None
big_balls = []
small_balls = []
boy_attacks = []


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def get_boy():
    return boy


def get_big_balls():
    return big_balls


def get_small_balls():
    return small_balls

def add_boy_attack(boy_attack):
    global boy_attacks
    boy_attacks.append(boy_attack)
    game_world.add_object(boy_attack, 1)

def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global zombie
    zombie = Zombie()
    game_world.add_object(zombie, 1)

    global big_balls
    big_balls = [BigBall() for i in range(5)]
    game_world.add_objects(big_balls, 1)

    global small_balls
    small_balls = [SmallBall() for i in range(5)]
    game_world.add_objects(small_balls, 1)


    ground = Ground()
    game_world.add_object(ground, 0)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if collide(boy, zombie):
        if len(big_balls) == 0 and len(small_balls) == 0:
            game_framework.change_state(end_state)
        else:
            game_world.remove_object(zombie)

    for ball in big_balls:
        if collide(zombie, ball):
            big_balls.remove(ball)
            game_world.remove_object(ball)
            zombie.add_hp(100)

    if len(big_balls) == 0:
        for ball in small_balls:
            if collide(zombie, ball):
                small_balls.remove(ball)
                game_world.remove_object(ball)
                zombie.add_hp(50)

    for boy_attack in boy_attacks:
        if collide(zombie, boy_attack):
            boy_attacks.remove(boy_attack)
            game_world.remove_object(boy_attack)
            zombie.add_hp(-100)






def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







from pico2d import *
import random

# 객체는 실제 세계에 존재하는 물체를 컴퓨터 프로그램으로 표현하기 위한 구조
# 추상화는 줄이고 간단히 하는 것
# 객체의 필요한 속성을 찾아주고(상태), 그 속성이 어떻게 변하는지 찾음(행위)
# 게임 내 객체는 3가지 이유에서 움직인다
# 1. 물리법칙 2. 지능 3. 사용자 입력
# 클래스: 객체를 생성해주는 문법적인 도구
# 클래스는 명사로 만들어라
# 왼쪽 하단에 파이썬 콘솔
# 선택: 객체마다 이름을 가질 필요가 있을까? 없다면 List Comprehension 이용

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        if random.randint(0, 1) == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')
        self.speed = random.randint(3, 10)

    def update(self):
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
team = [Boy() for i in range(11)]
balls = [Ball() for i in range(20)]
grass = Grass()

running = True

# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()

    for s_ball in balls:
        if s_ball.y > 60:
            s_ball.update()
        else:
            s_ball.y = 60


    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for s_ball in balls:
        s_ball.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()
# 이것은 각 상태들을 객체로 구현한 것임.
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5
TIME_PER_ACTION1 = 0.5
ACTION_PER_TIME1 = 1.0 / TIME_PER_ACTION1
FRAMES_PER_ACTION1 = 3
from pico2d import get_time, load_image, load_font, clamp,  SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import game_world
import game_framework
import random

# state event check
# ( state event type, event value )

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT

def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'

# time_out = lambda e : e[0] == 'TIME_OUT'




# Boy Run Speed
# fill here

# Boy Action Speed
# fill here





class Idle:

    @staticmethod
    def enter(boy, e):
        if boy.face_dir == -1:
            boy.action = 1
        elif boy.face_dir == 1:
            boy.action = 1
        boy.dir = 0
        boy.frame = 0
        boy.wait_time = get_time() # pico2d import 필요
        pass

    @staticmethod
    def exit(boy, e):
        if space_down(e):
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        boy.action = (boy.action + FRAMES_PER_ACTION1 * ACTION_PER_TIME1 * game_framework.frame_time) % 3
        boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x, boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 180, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 180,
                                          boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 360, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 360,
                                          boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 540, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 540,
                                          boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 720, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 720,
                                          boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x,
                                          boy.y - 200,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 180, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 180,
                                          boy.y - 200,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 360, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 360,
                                          boy.y - 200,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 540, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 540,
                                          boy.y - 200,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 720, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 720,
                                          boy.y - 200,
                                          180, 165)



class Run:

    @staticmethod
    def enter(boy, e):
        if right_down(e) or left_up(e): # 오른쪽으로 RUN
            boy.dir, boy.action, boy.face_dir = 1, 1, 1
        elif left_down(e) or right_up(e): # 왼쪽으로 RUN
            boy.dir, boy.action, boy.face_dir = -1, 1, -1

    @staticmethod
    def exit(boy, e):
        if space_down(e):
            boy.fire_ball()

        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        boy.action = (boy.action + FRAMES_PER_ACTION1 * ACTION_PER_TIME1 * game_framework.frame_time) % 3
        boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600-25)


    @staticmethod
    def draw(boy):
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x, boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 180, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 180,
                                          boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 360, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 360,
                                          boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 540, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 540,
                                          boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 720, boy.y)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 720,
                                          boy.y,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x,
                                          boy.y - 200,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 180, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 180,
                                          boy.y - 200,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 360, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 360,
                                          boy.y - 200,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 540, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 540,
                                          boy.y - 200,
                                          180, 165)
        if (boy.face_dir == 1):
            boy.image.clip_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, boy.x + 720, boy.y - 200)
        if (boy.face_dir == -1):
            boy.image.clip_composite_draw(int(boy.frame) * 180, int(boy.action) * 165, 180, 165, 0, 'h', boy.x + 720,
                                          boy.y - 200,
                                          180, 165)


class StateMachine:
    def __init__(self, boy):
        self.boy = boy
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, time_out : Idle, space_down: Idle},
            Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run}
        }

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.boy, e)
                self.cur_state = next_state
                self.cur_state.enter(self.boy, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.boy)





class Boy:
    def __init__(self):
        self.x, self.y = 0,600
        self.frame = 0
        self.action = 3
        self.face_dir = 1
        self.dir = 0
        self.font = load_font('ENCR10B.TTF', 16)

        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.item = 'Ball'


    def fire_ball(self):

        if self.item ==   'Ball':
            ball = Ball(self.x, self.y, self.face_dir*10)
            game_world.add_object(ball)
        elif self.item == 'BigBall':
            ball = BigBall(self.x, self.y, self.face_dir*10)
            game_world.add_object(ball)
        # if self.face_dir == -1:
        #     print('FIRE BALL LEFT')
        #
        # elif self.face_dir == 1:
        #     print('FIRE BALL RIGHT')

        pass

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))


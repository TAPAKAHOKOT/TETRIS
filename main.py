import turtle as tt
from settings import Settugs
from figures import Figures
import time
import numpy as np
import keyboard as kb
import sounddevice as sd
from threading import Thread
from ecvalaiser import Sub
import math as m

tt.tracer(0, 0)
tt.bgcolor("Black")


settings = Settugs()

drawer = tt.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.color("#{}".format("1a" * 3))


s_dwr = tt.Turtle()
s_dwr.hideturtle()
s_dwr.speed(0)

sub = Sub(settings.colors, s_dwr)
sub.run_callback()


def set_figs_type():
    settings.fig_types = [
        [
            np.array([[3, 4, 5], [
                settings.height - 1,
                settings.height - 1,
                settings.height - 1]]),
            np.array([[4, 4, 4], [
                settings.height - 2,
                settings.height - 1,
                settings.height]])
        ],

        [
            np.array([[3, 3, 4, 4], [
                settings.height - 1,
                settings.height - 2,
                settings.height - 1,
                settings.height - 2]])
        ],
        [
            np.array([[3, 4, 4], [
                settings.height - 1,
                settings.height - 1,
                settings.height - 2
            ]]),
            np.array([[3, 4, 4], [
                settings.height - 2,
                settings.height - 1,
                settings.height - 2
            ]]),
            np.array([[3, 3, 4], [
                settings.height - 1,
                settings.height - 2,
                settings.height - 2
            ]]),
            np.array([[3, 3, 4], [
                settings.height - 1,
                settings.height - 2,
                settings.height - 1
            ]]),

        ],
        [
            np.array([[3, 4, 4, 5], [
                settings.height - 1,
                settings.height - 1,
                settings.height - 2,
                settings.height - 1
            ]]),
            np.array([[4, 4, 4, 3], [
                settings.height,
                settings.height - 1,
                settings.height - 2,
                settings.height - 1
            ]]),
            np.array([[3, 4, 4, 5], [
                settings.height - 1,
                settings.height - 1,
                settings.height,
                settings.height - 1
            ]]),
            np.array([[4, 4, 4, 5], [
                settings.height,
                settings.height - 1,
                settings.height - 2,
                settings.height - 1
            ]]),


        ]


    ]


set_figs_type()

st_blocks = tt.Turtle()
st_blocks.hideturtle()
st_blocks.speed(0)


def mv(x, y, dwr):
    dwr.up()
    dwr.goto(x, y)
    dwr.down()


def box(x, y, dwr, d=False):
    mv(x + settings.size / 2, y + settings.size / 2, dwr)

    if d:
        dwr.fillcolor(fig.color)
        dwr.begin_fill()

    dwr.setheading(90)
    dwr.fd(settings.size)
    dwr.setheading(180)
    dwr.fd(settings.size)
    dwr.setheading(270)
    dwr.fd(settings.size)
    dwr.setheading(0)
    dwr.fd(settings.size)

    if d:
        dwr.end_fill()


t_dwr = tt.Turtle()
t_dwr.hideturtle()
t_dwr.speed(0)
t_dwr.color("Lime Green")

mv(-450, 370, t_dwr)
t_dwr.write("Score is {}".format(settings.score), False,
            align="left", font=("Arial", 8, "normal"))


fig = Figures(settings)
settings.figs.append(fig)


def m_left():
    if fig.zip_coors[0][0] > 0:
        fig.going_left()


def m_right():
    if fig.zip_coors[-1][0] < settings.width - 1:
        fig.going_right()


def m_down():
    settings.time_step = 1


def m_up():
    fig.pos += 1

    if fig.pos >= len(fig.main_coors):
        fig.pos = 0

    fig.coors = fig.main_coors[fig.pos]
    fig.zip_coors = list(zip(fig.coors[0], fig.coors[1]))


kb.add_hotkey('left', m_left)
kb.add_hotkey('right', m_right)
kb.add_hotkey('down', m_down)
kb.add_hotkey('up', m_up)

for k, row in enumerate(settings.window):
    for i, flow in enumerate(row):
        box(i * settings.size - settings.x_s,
            k * settings.size - settings.y_s, drawer)


while settings.rungame:

    if settings.time_counter % settings.time_step == 0:
        # drawer.clear()
        fig.dwr.clear()

        def del_line(line):
            settings.time_step_min -= 0.01
            settings.normal_time_step = m.floor(settings.time_step_min)
            print(settings.normal_time_step)
            settings.score += 10
            t_dwr.clear()
            t_dwr.write("Score is {}".format(settings.score), False,
                        align="left", font=("Arial", 8, "normal"))
            # print(settings.score)

            arr = []
            for k in settings.bottom:
                if k[1] > line:
                    arr.append([k[0], k[1] - 1])
                elif k[1] != line:
                    arr.append([k[0], k[1]])
            settings.bottom = arr[:]

            st_blocks.clear()
            for k, row in enumerate(settings.window):
                for i, flow in enumerate(row):
                    if [i, k] in settings.bottom:

                        box(i * settings.size - settings.x_s, k *
                            settings.size - settings.y_s, st_blocks, True)

        arr = sorted([[k[1], k[0]]
                      for k in settings.bottom])[settings.width:]
        # print(arr)

        n = 0

        for _ in range(3):
            n = 0
            for i, k in enumerate(arr):
                if i != 0:
                    if k[0] == arr[i - 1][0]:
                        n += 1

                        if n == settings.width - 1:
                            del_line(arr[i - 1][0])

                            n = 0
                            arr = sorted([[k[1], k[0]]
                                          for k in settings.bottom])[settings.width:]
                            break
                    else:
                        n = 0

        for x, y in fig.zip_coors:
            if [x, y - 1] in settings.bottom:
                for t, g in fig.zip_coors:
                    settings.bottom.append([t, g])
                    settings.time_step = settings.normal_time_step
                    box(t * settings.size - settings.x_s, g *
                        settings.size - settings.y_s, st_blocks, True)

                    if g >= settings.height - 2:
                        print("GAME OVER")
                        settings.rungame = False
                        break

                set_figs_type()
                fig = Figures(settings)

                break

        for k, row in enumerate(settings.window):
            for i, flow in enumerate(row):
                if (i, k) in fig.zip_coors:
                    box(i * settings.size - settings.x_s, k *
                        settings.size - settings.y_s, fig.dwr, True)

        fig.going_down()

    settings.time_counter += 1
    sub.draw()

    time.sleep(0.005)

    tt.update()

tt.mainloop()

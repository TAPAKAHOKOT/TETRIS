import turtle as tt
import numpy as np
from random import choice


class Figures:
    def __init__(self, settings):
        self.dwr = tt.Turtle()
        self.dwr.hideturtle()
        self.dwr.speed(0)

        self.pos = 0

        self.color = choice(settings.colors)

        self.main_coors = choice(settings.fig_types)
        self.coors = self.main_coors[self.pos]
        self.zip_coors = list(zip(self.coors[0], self.coors[1]))

    def going_down(self):
        for k in self.main_coors:
            k[1] -= 1

        self.coors = self.main_coors[self.pos]
        self.zip_coors = list(zip(self.coors[0], self.coors[1]))

    def going_left(self):
        for k in self.main_coors:
            k[0] -= 1

        self.coors = self.main_coors[self.pos]
        self.zip_coors = list(zip(self.coors[0], self.coors[1]))

    def going_right(self):
        for k in self.main_coors:
            k[0] += 1

        self.coors = self.main_coors[self.pos]
        self.zip_coors = list(zip(self.coors[0], self.coors[1]))

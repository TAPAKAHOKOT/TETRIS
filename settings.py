import numpy as np


class Settugs:
    def __init__(self):
        self.size = 30

        self.width = 8
        self.height = 24

        self.x_s = self.size * self.width // 2
        self.y_s = self.size * self.height // 2

        self.window = [[0] * self.width] * self.height

        self.figs = []
        self.score = 0

        self.rungame = True
        self.normal_time_step = 4
        self.time_step_min = self.normal_time_step
        self.time_step = self.normal_time_step

        self.time_counter = 0

        self.fig_types = []

        self.colors = [
            "Dodger Blue",
            "Deep Sky Blue",
            "Sky Blue",
            "Green",
            "Forest Green",
            "Olive Drab",
            "Goldenrod",
            "Gold",
            "Chocolate",
            "Firebrick",
            "Brown",
            "Violet Red",
            "Violet",
            "Plum",
            "Orchid",
            "Medium Orchid",
            "Tomato",
            "Orange Red",
            "Red"
        ]

        self.bottom = []
        for k in range(self.width):
            self.bottom.append([k, -1])

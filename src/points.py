import tkinter as tk
from nn_vis import CircleCoords
from constants import *


class Point:
    def __init__(self, relx, rely, class_):
        self.relx = relx
        self.rely = rely
        self.class_ = class_


class Points(tk.Canvas):
    def __init__(self, parent, nn):
        tk.Canvas.__init__(self, parent, bg=BG_COLOR,
                           highlightthickness=5, highlightbackground=FG_COLOR)

        self.points = []
        self.current_class = 0
        self.nn = nn

        self.bind("<Button>", self.on_click)
        self.bind("<B1-Motion>", self.on_left_drag)
        self.bind("<B3-Motion>", self.on_right_drag)

    def draw(self):
        self.delete('all')

        # Drawing points

        for point in self.points:
            coords = CircleCoords(point.relx * self.width,
                                  point.rely * self.height, POINT_RADIUS)
            self.create_oval(coords.x1, coords.y1, coords.x2,
                             coords.y2, fill=CLASS_0_COLOR if point.class_ == 0 else CLASS_1_COLOR)

        # Drawing decision boundary
        # On how to get function from perceptron : https://medium.com/@thomascountz/calculate-the-decision-boundary-of-a-single-perceptron-visualizing-linear-separability-c4d77099ef38

        w1 = self.nn.last_layer.weights[0, 0]
        w2 = self.nn.last_layer.weights[1, 0]
        b = self.nn.last_layer.biases[0, 0] - 0.5

        x1 = 0
        y1 = (-(b / w2) / (b / w1)) * x1 + (-b / w2)
        x2 = 1
        y2 = (-(b / w2) / (b / w1)) * x2 + (-b / w2)

        self.create_line(x1, y1 * self.height, self.width,
                         y2 * self.height, fill="white")

    @property
    def width(self):
        return self.winfo_width()

    @property
    def height(self):
        return self.winfo_height()

    def on_click(self, event):
        self.points.append(
            Point(event.x / self.width, event.y / self.height, 0 if event.num == 1 else 1))
        self.draw()

    def on_left_drag(self, event):
        self.points.append(
            Point(event.x / self.width, event.y / self.height, 0))
        self.draw()

    def on_right_drag(self, event):
        self.points.append(
            Point(event.x / self.width, event.y / self.height, 1))
        self.draw()

    def reset(self, nn):
        self.points = []
        self.nn = nn
        self.draw()

import tkinter as tk
from constants import *
from utils import from_rgb


class CircleCoords:
    def __init__(self, x=0, y=0, r=1):
        self.cx = x
        self.cy = y
        self.r = r
        self.x1 = x - r
        self.y1 = y - r
        self.x2 = x + r
        self.y2 = y + r


class NeuralNetVis(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent, bg=BG_COLOR,
                           highlightthickness=5, highlightbackground=FG_COLOR)

    def draw(self, nn):
        self.delete('all')

        r = min(50, self.width / 4 - 20, self.height /
                4 - 20)  # Neuron circle radius
        neurons_font = ("Arial", int(-r/2))

        # Drawing circles neurons

        i1 = CircleCoords(self.width * 1/4, self.height * 1/4, r)
        i2 = CircleCoords(self.width * 1/4, self.height * 3/4, r)
        o = CircleCoords(self.width * 3/4, self.height * 1/2, r)

        self.create_oval(i1.x1, i1.y1, i1.x2, i1.y2,
                         outline=FG_COLOR, fill=BG_COLOR, width=3)

        self.create_oval(i2.x1, i2.y1, i2.x2, i2.y2,
                         outline=FG_COLOR, fill=BG_COLOR, width=3)

        self.create_oval(o.x1, o.y1, o.x2, o.y2,
                         outline=FG_COLOR, fill=BG_COLOR, width=3)

        # Computing line color from weights

        i1_weight = nn.last_layer.weights[0, 0]
        i2_weight = nn.last_layer.weights[1, 0]

        i1_b = min(abs(i1_weight), 1)
        i2_b = min(abs(i2_weight), 1)

        i1_color = from_rgb(
            1, 1 - i1_b, 1 - i1_b) if i1_weight < 0 else from_rgb(1 - i1_b, 1 - i1_b, 1)
        i2_color = from_rgb(
            1, 1 - i2_b, 1 - i2_b) if i2_weight < 0 else from_rgb(1 - i2_b, 1 - i2_b, 1)

        # Drawing lines with computed colors

        self.create_line(i1.x2, i1.cy, o.x1, o.cy, fill=i1_color, width=3)
        self.create_line(i2.x2, i2.cy, o.x1, o.cy, fill=i2_color, width=3)

        # Drawing neurons text

        self.create_text(i1.cx, i1.cy, text="x",
                         fill=FG_COLOR, font=neurons_font)
        self.create_text(i2.cx, i2.cy, text="y",
                         fill=FG_COLOR, font=neurons_font)
        self.create_text(o.cx, o.cy, text="class",
                         fill=FG_COLOR, font=neurons_font)

    @property
    def width(self):
        return self.winfo_width()

    @property
    def height(self):
        return self.winfo_height()

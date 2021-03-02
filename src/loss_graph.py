import tkinter as tk
from constants import *


class LossGraphFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=BG_COLOR,
                          highlightthickness=5, highlightbackground=FG_COLOR)

        self.title = tk.Label(
            self, text="Loss / Error", font=("Arial", 15), bg=BG_COLOR, fg=FG_COLOR)
        self.title.pack(fill=tk.X)

        self.canvas = LossGraphCanvas(self)
        self.canvas.pack(expand=True, fill=tk.BOTH)

    def add_loss(self, loss):
        self.canvas.add_loss(loss)

    def reset(self):
        self.canvas.reset()


class LossGraphCanvas(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self, parent, bg=BG_COLOR)

        self.data = []
        self.all_time_max = 0

    def draw(self):
        self.delete("all")

        bottom = self.height - 20
        self.create_line(0, bottom, self.width, bottom, fill=FG_COLOR)

        if len(self.data) < 2:
            return

        x = self.width
        step = self.width/len(self.data)
        maxy = self.all_time_max
        for i in range(len(self.data) - 1, -1, -1):
            p = self.data[i]
            np = self.data[i - 1]

            self.create_line(x, bottom - p/maxy * self.height, x -
                             step, bottom - np/maxy * self.height, fill=FG_COLOR)

            x -= step

            if x < step:
                break

    def add_loss(self, loss):
        self.data.append(loss)
        if loss > self.all_time_max:
            self.all_time_max = loss

        if len(self.data) > MAX_LOSS_POINTS:
            self.data = self.data[1:]

    def reset(self):
        self.data = []
        self.all_time_max = 0
        self.draw()

    @property
    def width(self):
        return self.winfo_width()

    @property
    def height(self):
        return self.winfo_height()

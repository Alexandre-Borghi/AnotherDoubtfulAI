# Author : Alexandre Borghi
# Date : 03-2021

import tkinter as tk
from nn import NeuralNetwork
from nn_vis import NeuralNetVis
from points import Points
from settings_frame import SettingsFrame
from loss_graph import LossGraphFrame
from random import choice, shuffle
from constants import *

# Palette : https://flatuicolors.com/palette/defo


def reset():
    global perceptron
    perceptron = NeuralNetwork([2, 1])
    nn_canvas.draw(perceptron)
    points.reset(perceptron)
    loss.reset()


root = tk.Tk()
root.attributes('-zoomed', True)
root.title("Binary Classifier Visualization")
root.config(bg=BG_COLOR)


perceptron = NeuralNetwork([2, 1])


nn_canvas = NeuralNetVis(root)
nn_canvas.place(relx=1/3, rely=0.5, relwidth=2/3, relheight=0.5)
nn_canvas.update()
nn_canvas.draw(perceptron)

points = Points(root, perceptron)
points_side = root.winfo_width() * 1/3
points.place(relx=0, rely=0, relwidth=1/3, height=points_side)
points.update()
points.draw()

settings = SettingsFrame(root, reset)
settings.place(relx=0, y=points_side, relwidth=1/3,
               height=root.winfo_height() - points_side)

loss = LossGraphFrame(root)
loss_side = root.winfo_height() / 2
loss.place(relx=1/3, rely=0, width=loss_side, relheight=1/2)


# Handling resize

def resize(event):
    nn_canvas.draw(perceptron)
    points_side = root.winfo_width() * 1/3
    points.place(height=points_side)
    points.update()
    points.draw()


# Function called to train neural network

def update():
    root.after(20, update)

    if len(points.points) == 0:
        return

    # rnd = list(points.points)
    # shuffle(rnd)

    # for p in rnd:
    #    perceptron.train([p.relx, p.rely], [p.class_], 0.1)

    for _ in range(1):
        p = choice(points.points)
        perceptron.train([p.relx, p.rely], [p.class_], settings.get_lr())
        loss.add_loss(perceptron.loss)

    nn_canvas.draw(perceptron)
    points.draw()
    loss.canvas.draw()


root.bind('<Configure>', resize)
root.after(100, update)
root.mainloop()

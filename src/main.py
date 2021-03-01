# Author : Alexandre Borghi
# Date : 03-2021

import tkinter as tk
from nn import NeuralNetwork
from nn_vis import NeuralNetVis

# Palette : https://flatuicolors.com/palette/defo

root = tk.Tk()
root.attributes('-zoomed', True)
root.title("Binary Classifier Visualization")


perceptron = NeuralNetwork([2, 1])


nn_canvas = NeuralNetVis(root)
nn_canvas.place(relx=1/3, rely=0.5, relwidth=2/3, relheight=0.5)
nn_canvas.update()
nn_canvas.draw(perceptron)


# Handling resize

def resize(event):
    nn_canvas.draw(perceptron)


root.bind('<Configure>', resize)
root.mainloop()

import tkinter as tk
from constants import *


class SettingsFrame(tk.Frame):
    def __init__(self, parent, reset_command):
        tk.Frame.__init__(self, parent, bg=BG_COLOR,
                          highlightthickness=5, highlightbackground=FG_COLOR)

        self.lr_slider = tk.Scale(
            self, from_=0.001, to=0.1, resolution=0.001, orient=tk.HORIZONTAL)
        self.lr_slider.set(0.1)
        self.lr_slider.place(relx=0.01, rely=0.01,
                             relwidth=0.98, relheight=0.1)

        self.reset_btn = tk.Button(
            self, text="Reset", command=reset_command)
        self.reset_btn.place(relx=0.01, rely=0.12,
                             relwidth=0.98, relheight=0.1)

    def get_lr(self):
        return self.lr_slider.get()

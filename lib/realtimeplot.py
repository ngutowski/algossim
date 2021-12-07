# -*- coding: utf-8 -*-
"""
Created on 2015

@author: Anthony Zhang - Uberi : https://gist.github.com/Uberi/283a13b8a71a46fb4dc8
"""
from collections import deque


class RealtimePlot:
    def __init__(self, axes, max_entries):
        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = deque(maxlen=max_entries)
        self.axes = axes
        self.max_entries = max_entries
        self.lineplot, = axes.plot([], [], "ro-")
        self.axes.set_autoscaley_on(True)

    def add(self, x, y):
        self.axis_x.append(x)
        self.axis_y.append(y)
        self.lineplot.set_data(self.axis_x, self.axis_y)
        self.axes.set_xlim(self.axis_x[0], self.axis_x[-1] + 1e-15)
        self.axes.relim()
        self.axes.autoscale_view()  # rescale the y-axis

    # def animate(self, figure, callback, interval = 50):
    #    import matplotlib.animation as animation
    #    def wrapper(frame_index):
    #        self.add(*callback(frame_index))
    #        self.axes.relim(); self.axes.autoscale_view() # rescale the y-axis
    #        return self.lineplot
    #    animation.FuncAnimation(figure, wrapper, interval=interval)

#!/usr/bin/python3

from gi.repository import Gtk

from matplotlib.figure import Figure
from numpy import arange, pi, random, linspace
import matplotlib.cm as cm
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

class Signals:
    def on_window1_destroy(self, widget):
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_objects_from_file('matplotlibwindow-glade.glade', ('window1', '') )
builder.connect_signals(Signals())

myfirstwindow = builder.get_object('window1')
sw = builder.get_object('scrolledwindow1')

fig = Figure(figsize=(5,5), dpi=100)
ax = fig.add_subplot(111, projection='polar')

N = 20
theta = linspace(0.0, 2 * pi, N, endpoint=False)
radii = 10 * random.rand(N)
width = pi / 4 * random.rand(N)

bars = ax.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(cm.jet(r / 10.))
    bar.set_alpha(0.5)

ax.plot()

canvas = FigureCanvas(fig)
sw.add_with_viewport(canvas)

myfirstwindow.show_all()
Gtk.main()

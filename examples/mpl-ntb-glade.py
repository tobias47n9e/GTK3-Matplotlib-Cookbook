#!/usr/bin/python3

from gi.repository import Gtk

from matplotlib.figure import Figure
from numpy import sin, cos, pi, linspace
#Possibly this rendering backend is broken currently
#from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
from matplotlib.backends.backend_gtk3 import NavigationToolbar2GTK3 as NavigationToolbar

class Signals:
    def on_window1_destroy(self, widget):
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_objects_from_file('mpl-ntb-glade.glade', ('window1', '') )
builder.connect_signals(Signals())

myfirstwindow = builder.get_object('window1')
sw = builder.get_object('scrolledwindow1')
sw2 = builder.get_object('scrolledwindow2')

fig = Figure(figsize=(5,5), dpi=80)
ax = fig.add_subplot(111)

n = 1000
xsin = linspace(-pi, pi, n, endpoint=True)
xcos = linspace(-pi, pi, n, endpoint=True)
ysin = sin(xsin)
ycos = cos(xcos)

sinwave = ax.plot(xsin, ysin, color='black', label='sin(x)')
coswave = ax.plot(xcos, ycos, color='black', label='cos(x)', linestyle='--')

ax.set_xlim(-pi,pi)
ax.set_ylim(-1.2,1.2)

ax.fill_between(xsin, 0, ysin, (ysin - 1) > -1, color='blue', alpha=.3)
ax.fill_between(xsin, 0, ysin, (ysin - 1) < -1, color='red',  alpha=.3)
ax.fill_between(xcos, 0, ycos, (ycos - 1) > -1, color='blue', alpha=.3)
ax.fill_between(xcos, 0, ycos, (ycos - 1) < -1, color='red',  alpha=.3)

ax.legend(loc='upper left')

ax = fig.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

fig.tight_layout()

canvas = FigureCanvas(fig)
sw.add_with_viewport(canvas)

toolbar = NavigationToolbar(canvas, myfirstwindow)
sw2.add_with_viewport(toolbar)

myfirstwindow.show_all()
Gtk.main()

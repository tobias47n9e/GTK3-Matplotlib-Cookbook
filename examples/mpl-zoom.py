#!/usr/bin/python3

from gi.repository import Gtk
from matplotlib.figure import Figure
from numpy import random
from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3 import NavigationToolbar2GTK3 as NavigationToolbar
from matplotlib.patches import Rectangle

class DrawPoints:
    '''Creates random points, 2 axis on 1 figure on 1 canvas on init. Allows for drawing and zooming of points.'''
    def __init__(self):
        self.n = 20
        self.xrand = random.rand(1, self.n)*10
        self.yrand = random.rand(1, self.n)*10
        self.randsize = random.rand(1, self.n)*200
        self.randcolor = random.rand(self.n, 3)

        self.fig = Figure(figsize=(10, 10), dpi=80)
        self.ax = self.fig.add_subplot(121)
        self.axzoom = self.fig.add_subplot(122)
        self.canvas = FigureCanvas(self.fig)
    def draw(self):
        '''Draws the ax-subplot'''
        self.ax.cla()
        self.ax.grid(True)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.scatter(self.xrand, self.yrand, marker='o', s=self.randsize, c=self.randcolor, alpha=0.5)
    def drawzoom(self):
        '''Draws the axzoom-suplot'''
        self.axzoom.cla()
        self.axzoom.grid(True)
        self.axzoom.set_xlim(self.x-1, self.x+1)
        self.axzoom.set_ylim(self.y-1, self.y+1)
        self.axzoom.scatter(self.xrand, self.yrand, marker='o', s=self.randsize*5, c=self.randcolor, alpha=0.5)
    def zoom(self, x, y):
        '''Adds a rectangle to the zoomed area of the ax-graph and updates the axzoom-graph'''
        self.x = x
        self.y = y
        self.draw()
        self.drawzoom()
        self.ax.add_patch(Rectangle((x - 1, y - 1), 2, 2, facecolor="grey", alpha=0.2))
        self.fig.canvas.draw()
      
def updatecursorposition(event):
    '''When cursor inside plot, get position and print to statusbar'''
    if event.inaxes:
        x = event.xdata
        y = event.ydata
        statbar.push(1, ("Coordinates:" + " x= " + str(round(x, 3)) + "  y= " + str(round(y, 3))))

def updatezoom(event):
    '''When mouse is right-clicked on the canvas get the coordiantes and send them to points.zoom'''
    if event.button!=1: return
    if (event.xdata is None): return
    x,y = event.xdata, event.ydata
    points.zoom(x,y)

window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(800, 500)
window.set_title('Matplotlib')

box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
window.add(box)

points = DrawPoints()
points.draw()

box.pack_start(points.canvas, True, True, 0)

toolbar = NavigationToolbar(points.canvas, window)
box.pack_start(toolbar, False, True, 0)

statbar = Gtk.Statusbar()
box.pack_start(statbar, False, True, 0)

points.fig.canvas.mpl_connect('motion_notify_event', updatecursorposition)
points.fig.canvas.mpl_connect('button_press_event', updatezoom)

window.show_all()
Gtk.main() 

#!/usr/bin/python3

from gi.repository import Gtk
from matplotlib.figure import Figure
#Possibly this rendering backend is broken currently
#from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

class MainClass(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Matplotlib")
        self.set_default_size(800, 500)
        self.boxvertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.connect("delete-event", Gtk.main_quit)
        self.add(self.boxvertical)
        
        self.toolbar = Gtk.Toolbar()
        self.context = self.toolbar.get_style_context()
        self.context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)
        self.boxvertical.pack_start(self.toolbar, False, False, 0)

        self.addbutton = Gtk.ToolButton(Gtk.STOCK_ADD)
        self.removebutton = Gtk.ToolButton(Gtk.STOCK_REMOVE)

        self.toolbar.insert(self.addbutton, 0)
        self.toolbar.insert(self.removebutton, 1)

        self.box = Gtk.Box()
        self.boxvertical.pack_start(self.box, True, True, 0)
        
        self.fig = Figure(figsize=(10,10), dpi=80)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.box.pack_start(self.canvas, True, True, 0)

        self.addbutton.connect("clicked", self.addrow)
        self.removebutton.connect("clicked", self.removerow)
        
        self.liststore = Gtk.ListStore(float, float)
        self.treeview = Gtk.TreeView(model=self.liststore)
        self.box.pack_start(self.treeview, False, True, 0)

        self.xrenderer = Gtk.CellRendererText()
        self.xrenderer.set_property("editable", True)
        self.xcolumn = Gtk.TreeViewColumn("x-Value", self.xrenderer, text=0)
        self.xcolumn.set_min_width(100)
        self.xcolumn.set_alignment(0.5)
        self.treeview.append_column(self.xcolumn)
        
        self.yrenderer = Gtk.CellRendererText()
        self.yrenderer.set_property("editable", True)
        self.ycolumn = Gtk.TreeViewColumn("y-Value", self.yrenderer, text=1)
        self.ycolumn.set_min_width(100)
        self.ycolumn.set_alignment(0.5)
        self.treeview.append_column(self.ycolumn)

        self.xrenderer.connect("edited", self.xedited)
        self.yrenderer.connect("edited", self.yedited)

        self.liststore.append([2.35, 2.40])
        self.liststore.append([3.45, 4.70])

    def resetplot(self):
        self.ax.cla()
        self.ax.set_xlim(0,10)
        self.ax.set_ylim(0,10)
        self.ax.grid(True)

    def plotpoints(self):
        self.resetplot()
        for row in self.liststore:
            self.ax.scatter(row[:1], row[1:], marker='o', s=50)
        self.fig.canvas.draw()

    def xedited(self, widget, path, number):
        self.liststore[path][0] = float(number.replace(',', '.'))
        self.plotpoints()
        
    def yedited(self, widget, path, number):
        self.liststore[path][1] = float(number.replace(',', '.'))
        self.plotpoints()

    def addrow(self, widget):
        self.liststore.append()
        self.plotpoints()

    def removerow(self, widget):
        self.select = self.treeview.get_selection()
        self.model, self.treeiter = self.select.get_selected()
        if self.treeiter is not None:
            self.liststore.remove(self.treeiter)
        self.plotpoints()

mc = MainClass()
mc.resetplot()
mc.plotpoints()

mc.show_all()
Gtk.main()

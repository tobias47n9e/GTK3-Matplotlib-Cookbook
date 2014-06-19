#!/usr/bin/python3

from gi.repository import Gtk

class Signals:
    def on_window1_destroy(self, widget):
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_objects_from_file('empty-window-glade.glade', ('window1', '') )
builder.connect_signals(Signals())

myfirstwindow = builder.get_object('window1')

myfirstwindow.show_all()
Gtk.main()

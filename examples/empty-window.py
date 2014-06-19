#!/usr/bin/python3

from gi.repository import Gtk

myfirstwindow = Gtk.Window()

myfirstwindow.connect("delete-event", Gtk.main_quit)
myfirstwindow.show_all()
Gtk.main()

#!/usr/bin/python3

from gi.repository import Gtk

my_first_window = Gtk.Window()

my_first_window.connect("delete-event", Gtk.main_quit)
my_first_window.show_all()
Gtk.main()

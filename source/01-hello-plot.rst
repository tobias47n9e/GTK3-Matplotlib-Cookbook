.. _helloplot:

Hello plot!
============

The first chapter will explain how to open an empty GTK3-window and then how to embed Matplotlib into it.

For small applications the GTK3-code can be easily integrated into the Python-code. Building the interface with Glade is a little more complicated in the beginning. With increasing size though, the usage of Glade will become more useful.

Empty window (GTK3)
-------------------
Let's start with the code that will open an empty window.

::
    
    #!/usr/bin/python3
    
    from gi.repository import Gtk
    
    myfirstwindow = Gtk.Window()
    
    myfirstwindow.connect("delete-event", Gtk.main_quit)
    myfirstwindow.show_all()
    Gtk.main()
    
These are all the lines that are required for a fully functional window. This is what they do:

The first line helps Unix operating systems to recognize the file format of a file. In this case we wan't the operating system to know that the file should be excecuted with Python 3.x:

::

    #!/usr/bin/python3

Then the program needs to import the gui-framework (or gui-toolkit). Older Gtk 2.x applications used (*import gtk*), but for Python 3 and Gtk 3.x applications (i.e. this tutorial) we need:

::

    from gi.repository import Gtk

We can then define an object for a *Gtk.Window()*, which can have any name:

::

    myfirstwindow = Gtk.Window()
    
Next the we have to connect our program with the quit-button (x-button) of the window. Otherwise closing the window will not terminate the application:

::

    myfirstwindow.connect("delete-event", Gtk.main_quit)


The next line ensures that the program window is shown. Excluding this line will mean that the program start, but no window is displayed:

::
    myfirstwindow.show_all()

The last line starts the main program loop with all functions. Without this line no loop is started and the program will not do anything:

::
    Gtk.main()
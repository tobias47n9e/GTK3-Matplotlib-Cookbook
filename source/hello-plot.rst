.. _hello-plot:

Hello plot!
============
The first chapter will explain how to open an empty GTK3-window and then how to embed Matplotlib into it.

For small applications the GTK3-code can be easily integrated into the Python-code. Building the interface with Glade is a little more complicated in the beginning. With increasing size though, the usage of Glade will become more useful.

Empty GTK 3 window
------------------
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

Empty window with Glade
^^^^^^^^^^^^^^^^^^^^^^^
Opening an empty window with Glade takes a little more effort. First we need to open the Glade interface designer. Then drag a *GtkWindow* into the workspace. By default the window will be named *"window1"*, which we can keep. Then we have to set a signal for that window, so we can later close it. The signal we need is *"GtkWidget --> destroy"* and in the column process we can set *"on_window1_destroy"*. This will also be the name of the function in the Python code.

.. figure:: _static/empty-window-glade.png
    :width: 400px
    :align: center
    :alt: Glade-screenshot

    The steps in Glade are: Create a *GtkWindow*, then open the Signals tab and enter *"on_window1_destroy"* for *"GtkWidget --> destroy"*.

This is all we need for an empty (and closable) window. Then we can save the file with the extension *".glade"*. The finished XML-code of that file looks like this and should be fairly easy to understand:

::

    <?xml version="1.0" encoding="UTF-8"?>
    <!-- Generated with glade 3.16.1 -->
    <interface>
      <requires lib="gtk+" version="3.10"/>
      <object class="GtkWindow" id="window1">
        <property name="can_focus">False</property>
        <signal name="destroy" handler="on_window1_destroy" swapped="no"/>
        <child>
          <placeholder/>
        </child>
      </object>
    </interface>
    
Now we have to create a separate file to hold the python code that will call the Glade-file. The finished code looks like this:

::

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
    
In comparison to the previous approach a few lines of code have changed. First we call the *Gtk.Builder()* function:

::

    builder = Gtk.Builder()

Then we use the *Gtk.Builder()* to add the objects from the Glade-file. In the bracket we first need to specify the Glade-file, and then a list of objects even if we just want to call one object (*Thankyou errol from http://www.gtkforums.com for this tip*):

::

    builder.add_objects_from_file('empty-window-glade.glade', ('window1', '') )
    
Next the builder needs to connect the signals that we defined in the Glade file. The easiest way of doing this is to place the Signals in their own *Class*. We only defined one signal in Glade which was *"on_window1_destroy"*:
    
::

    builder.connect_signals(Signals())

    class Signals:
        def on_window1_destroy(self, widget):
            Gtk.main_quit()
            
The last two lines of the program are the same as for the previous example.

Further Reading
^^^^^^^^^^^^^^^^^^^^^^^
 - `Python GTK+ 3 Tutorial: Getting started <http://python-gtk-3-tutorial.readthedocs.org/en/latest/introduction.html>`_
 - `GTK+ 3 Reference Manual <https://developer.gnome.org/gtk3/>`_
 - `GTK+ 3 Reference Manual: GtkBuilder <https://developer.gnome.org/gtk3/stable/GtkBuilder.html>`_
 - `Glade - A user interface designer <https://glade.gnome.org/>`_

Embedding Matplotlib
--------------------
Now that we have an empty window we will learn how to place Matplotlib into it. The main differences are that we need to import Matplotlib-specific packages, insert our Matplotlib-code and place the resulting *FigureCanvas* in a *Gtk.ScrolledWindow* (which is a child-element of the *Gtk.Window*).

We will look at an example that will produce a random radial plot on each application start (adapted from http://matplotlib.org/dev/examples/pie_and_polar_charts/polar_bar_demo.html). The finished  Python-code is:

::

    #!/usr/bin/python3

    from gi.repository import Gtk

    from matplotlib.figure import Figure
    from numpy import arange, pi, random, linspace
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas

    myfirstwindow = Gtk.Window()
    myfirstwindow.connect("delete-event", Gtk.main_quit)
    myfirstwindow.set_default_size(400, 400)

    fig = Figure(figsize=(5,5), dpi=100)
    ax = fig.add_subplot(111, polar=True)

    N = 20
    theta = linspace(0.0, 2 * pi, N, endpoint=False)
    radii = 10 * random.rand(N)
    width = pi / 4 * random.rand(N)

    bars = ax.bar(theta, radii, width=width, bottom=0.0)

    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.5)

    ax.plot()

    sw = Gtk.ScrolledWindow()
    myfirstwindow.add(sw)

    canvas = FigureCanvas(fig)
    canvas.set_size_request(400,400)
    sw.add_with_viewport(canvas)

    myfirstwindow.show_all()
    Gtk.main()
    
.. figure:: _static/firstwindow.png
    :width: 200px
    :align: center
    :alt: GTK window with Matplotlib screenshot

    The first window with an embedded Matplotlib-graph as it renders in Ubuntu 14.04.

Embedding Matplotlib with Glade
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Recreating the previous example with Glade requires just some minor changes to the Glade-file and a slightly different Python-3-code.

First we need to add a *GtkScrolledWindow* to our empty window. Although the name has "window" in it, it actually is more like a canvas for other widgets. In the Python code we will place in the next step a *FigureCanvas* into the *GtkScrolledWindow*. In order to give the plot more space, we can also set the default width and height of *"window1"* to 400 px each.

.. figure:: _static/matplotlibwindow-glade.png
    :width: 400px
    :align: center
    :alt: Glade-screenshot

    Starting with the previous example all we need to add is a *GtkScrolledWindow*.

The XML-code of the Glade-file after the modifications looks like this:

::

    <?xml version="1.0" encoding="UTF-8"?>
    <!-- Generated with glade 3.16.1 -->
    <interface>
      <requires lib="gtk+" version="3.10"/>
      <object class="GtkWindow" id="window1">
        <property name="can_focus">False</property>
        <property name="default_width">400</property>
        <property name="default_height">400</property>
        <signal name="destroy" handler="on_window1_destroy" swapped="no"/>
        <child>
          <object class="GtkScrolledWindow" id="scrolledwindow1">
            <property name="visible">True</property>
            <property name="can_focus">True</property>
            <property name="shadow_type">in</property>
            <child>
              <placeholder/>
            </child>
          </object>
        </child>
      </object>
    </interface>

Starting with the code from the previous examples we only have to make slight changes to port this example. This is the final result:

::

    #!/usr/bin/python3
    
    from gi.repository import Gtk
    
    from matplotlib.figure import Figure
    from numpy import arange, pi, random, linspace
    import matplotlib.pyplot as plt
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
    ax = fig.add_subplot(111, polar=True)
    
    N = 20
    theta = linspace(0.0, 2 * pi, N, endpoint=False)
    radii = 10 * random.rand(N)
    width = pi / 4 * random.rand(N)
    
    bars = ax.bar(theta, radii, width=width, bottom=0.0)
    
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.5)
    
    ax.plot()
    
    canvas = FigureCanvas(fig)
    sw.add_with_viewport(canvas)
    
    myfirstwindow.show_all()
    Gtk.main()


Further Reading
^^^^^^^^^^^^^^^^^^^^^^^
 - `The Python Standard Library: Built-in Functions: zip <https://docs.python.org/3/library/functions.html#zip>`_
 - `Numpy <http://www.numpy.org/>`_
 - `The Matplotlib API: pyplot <http://matplotlib.org/api/pyplot_api.html>`_
 - `The Matplotlib API: figure <http://matplotlib.org/api/figure_api.html>`_
 - `Pyplot tutorial <http://matplotlib.org/users/pyplot_tutorial.html>`_
 - `Numpy Manual: linspace <http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html>`_
 - FigureCanvasGTK3Agg documentation [[2014-06-21 Find link for documentation]]
 
 
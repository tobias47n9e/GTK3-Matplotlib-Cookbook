.. gtk3-matplotlib-cookbook documentation master file, created by
   sphinx-quickstart on Thu Jun 19 16:22:54 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============
:Copyright: GNU Free Documentation License 1.3 with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts

This Cookbook explains how to embed Matplotlib into GTK3 using Python 3. The tutorials will start out simple, and slowly increase in difficulty. The examples will focus on education and application of mathematics and science. The goal is to make the reader a independent developer of scientific applications that process and graph data.

If you would like to add your own examples to this tutorial, please create an issue or pull-request at the github repository (https://github.com/spiessbuerger/GTK3-Matplotlib-Cookbook).

.. figure:: _static/firstwindow.png
    :width: 200px
    :align: center
    :alt: First window with embedded Matplotlib

Requirements
------------
To follow the examples you should have access to GTK+ 3.x, Python 3.x, Matplotlib 1.3.x and Glade 3.16.x or a more recent version.

Recommended reading
-------------------
In order to follow along with the Cookbook it is recommended to go through a Python 3.x tutorial (e.g. `https://docs.python.org/3.4/tutorial/ <https://docs.python.org/3.4/tutorial/>`_) and a tutorial about the Python bindings of GTK 3.x (e.g. http://python-gtk-3-tutorial.readthedocs.org/).

Additional reading:

 - Matplotlib

   - http://wiki.scipy.org/Cookbook/Matplotlib

 - Scientific Python

   - http://scipy-lectures.github.io/
   
 - GTK3 Reference
   
   - https://lazka.github.io/pgi-docs/Gtk-3.0/index.html   


News and Comments
-----------------
2014-12-26
^^^^^^^^^^
I have been busy on some other projects lately. Revisiting this project, I had some trouble running my examples on Ubuntu 14.04 and the current master of Matplotlib (1.5.dev1). The problem seems to be in the *gtk3agg* backend. I get the following error: *NotImplementedError: Surface.create_for_data: Not Implemented yet.*. Not sure how many people have trouble with this, but it is mentioned in different places (e.g. http://matplotlib.1069221.n5.nabble.com/Matplotlib-py3-gtk3-td42953.html). Getting the plots to work again just requires you to switch rendering backends:

    from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

2014-07-26
^^^^^^^^^^
The fourth chapter about entering data is finished. I also decided to start code reviewing with Landscape. The score was 63 % on standard settings and 23 % on high (meaning very strict code reviewing). The low score is mostly caused by the *conf.py* file from Sphinx, my usage of "old classes" and Landscape complaining about the Gtk specific code. I will try to deal with the issues first, before uploading more chapters.

2014-06-27
^^^^^^^^^^
Third chapter about zooming closer to datapoints is done. Currently I am just adding examples when I'm pleased with them. I will reorganize the book once the content is done. The new example relies heavily on classes. Does anybody reading this think that the amount of explanation is sufficient?

2014-06-19
^^^^^^^^^^
This Cookbook is not finished and will be gradually developed in the coming months. If you would like to participate you can mail me or fork the repository. I am a beginning programmer, so the presented code might not be optimal. If you find any sub-optimal sections please write me, or create an issue or pull request on Github.

Directory
---------
.. toctree::
   :numbered:
   :maxdepth: 2
   
   hello-plot
   matplotlib-toolbar
   zooming
   enteringdata

Indices and tables
==================
-* :ref:`genindex`
-* :ref:`modindex`
* :ref:`search`




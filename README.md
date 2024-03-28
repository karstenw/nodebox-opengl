<!-- $theme: default -->

### NodeBox for OpenGL


NodeBox for OpenGL (NOGL) is a Python module for creating 2D interactive visuals using OpenGL. It is based on the command set of the classic NodeBox for Mac OS X (http://nodebox.net). It has support for Bezier paths, text, image filters (blur, bloom, ...), offscreen rendering, animation & motion tweening, and simple 2D physics. Its purpose is to implement a small game engine for "City In A Bottle" (http://cityinabottle.org).

#### VERSION

1.8

#### LICENSE

BSD, see LICENSE.txt for further details.

#### REQUIREMENTS

- Python 3.11 : an installer can be downloaded from http://www.python.org/download/
- Pyglet 1.5.28  : an installer can be downloaded from http://www.pyglet.org/
	- It must be exactly version 1.5.28!

Your video hardware needs support for OpenGL 2.0.
If this is not the case, try updating to a new driver.


#### ATTENTION

This fork has been renamed "nodeboxgl" for coexistence with the NodeBox1 console install.

You import the commands with:

```python
from nodeboxgl.graphics import *
```


INSTALLATION
============

Run:

`python3 setup.py install`

in the nodeboxgl directory.


USAGE
=====

- For users coming from NodeBox for Mac OS X: this NodeBox for OpenGL does not have a built-in code editor. You can use the IDLE editor bundled with Python. On Mac OS X, we prefer TextMate (http://macromates.com).
- From the command line, you can run a script with: python example.py (or command-R in TextMate)
- This will open an application window with the output of your script.

Here is a simple NodeBox script:
```python
from nodeboxgl.graphics import *
def draw(canvas):
    canvas.clear()
    translate(250, 250)
    rotate(canvas.frame)
    rect(x=-50, y=-50, width=100, height=100)
canvas.size = 500, 500
canvas.run(draw)
```

It imports the nodebox.graphics module with the standard set of drawing commands. It defines a draw() function and attaches it to the canvas, so that it will be drawn each animation frame. It opens the main application window with canvas.run().

DOCUMENTATION
=============

http://cityinabottle.org/nodebox

ACKNOWLEDGEMENTS
================

Author: 
- Tom De Smedt (tom@organisms.be)

Contributing authors:
- Frederik De Bleser
- Lieven Menschaert
- Giorgio Olivero

Contributors:
- Karsten Wolf
- Tuk Bredsdorff

City In A Bottle:
- Nicolas Marinus
- Ludivine Lechat
- Tim Vets
- Frederik De Bleser
- Tom De Smedt

Copyright (c) 2008-2012 City In A Bottle

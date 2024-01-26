import os, sys; sys.path.insert(0, os.path.join("..",".."))

from nodeboxgl.graphics import *

# A freehand drawing application!

# The canvas, which is passed to every draw() call,
# has a "mouse" property that logs the current mouse state.
# Ideally, you'd use event handlers such as canvas.on_mouse_press()
# but we can already play around with the mouse here:
# - canvas.mouse.x: horizontal postion of the mouse, 0 means left canvas edge,
# - canvas.mouse.y: vertical postion of the mouse, 0 means bottom canvas edge,
# - canvas.mouse.dx: horizontal offset from the previous mouse position,
# - canvas.mouse.dy: vertical offset from the previous mouse position,
# - canvas.mouse.button: mouse button pressed (LEFT | MIDDLE | RIGHT | None),
# - canvas.mouse.modifiers: a list of keyboard modifiers (CTRL | SHIFT | ALT),
# - canvas.mouse.pressed: True when a button is pressed,
# - canvas.mouse.dragged: True when the mouse is dragged.
lastx, lasty = 0,0
def draw(canvas):
    global lastx, lasty
    if canvas.frame == 1:
        canvas.clear()
        # background( (0.6,0.2,0.2) )
        background( (1.0,1.0,1.0) )
    
    m = canvas.mouse
    x, y = m.x, m.y
    p = m.pressed

    strokewidth(1)
    if CTRL in m.modifiers:
        # If the CTRL key is held down, draw thinner lines.
        stroke(0, 0.2)
    else:
        stroke(0, 0.4)    
    
    if p:
        # If the mouse is pressed, draw lines.
        # This is a better way than simply drawing a dot at the current mouse position
        # (i.e. ellipse(m.x, m.y, 2, 2)), because the mouse can move faster
        # than the application can track. 
        # So each frame we draw a little line to the previous mouse position.
        #
        # 2017-06-14 kw 
        #   Changed from using m.dx, m.dy to manually updating lastx & lasty.
        #   m.dx, m.dy has too many holes in path
        
        line(lastx, lasty, x, y )
    lastx, lasty = x, y
canvas.size = 800, 600
canvas.run( draw )

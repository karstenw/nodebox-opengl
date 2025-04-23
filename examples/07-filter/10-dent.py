from nodeboxgl.graphics import *

import os
if os.path.exists("__DEBUG__"):
    img = Image("grid.png")
else:
    img = Image("creature.png")
X,Y = img.width, img.height

def draw(canvas):
    
    # This basically does the same as the previous example (bump),
    # except that we use a twirl distortion filter.
    # Furthermore, the filter is permanently applied when the mouse is pressed.
    # To do this, we replace the source image with the twirled version.
    # Hence we declare img as global, so we can modify the variable's contents.
    global img
    
    canvas.clear()
    
    dx = canvas.mouse.x / float(canvas.width)
    dy = canvas.mouse.y / float(canvas.height)
    if canvas.mouse.pressed:
        image( dent(img, dx, dy, radius=0.3, zoom=0.6) )
    else:
        image( dent(img, dx, dy, radius=0.15, zoom=0.3) )
# Start the application:
canvas.fps  = 60
canvas.size = X, Y
canvas.run(draw)

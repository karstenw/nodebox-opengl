from nodeboxgl.graphics import *

import os
if os.path.exists("__DEBUG__"):
    img = Image("grid.png")
else:
    img = Image("creature.png")
X,Y = img.width, img.height

def draw(canvas):
    canvas.clear()
    
    dx = canvas.mouse.x / float(canvas.width)
    dy = canvas.mouse.y / float(canvas.height)
    if canvas.mouse.pressed:
        # When the mouse is pressed, render a twirled version of the image,
        # and set it as the new source image.
        image( splash(img, dx, dy, radius=0.667), x=ox, y=oy )
    else:
        image( splash(img, dx, dy, radius=0.334), x=ox, y=oy )


# Start the application:
canvas.fps  = 60
canvas.size = X, Y
ox,oy = 0,0
canvas.run(draw)

from nodeboxgl.graphics import *

import os
if os.path.exists("__DEBUG__"):
    img = Image("grid.png")
else:
    img = Image("creature.png")
X,Y = img.width, img.height

def draw(canvas):
    canvas.clear()
    
    if canvas.mouse.pressed:
        image( fisheye( img,
                        canvas.mouse.relative_x,
                        canvas.mouse.relative_y,
                        radius=1.6,
                        zoom=1.6) )
    else:
        image( img )


# Start the application:
canvas.fps  = 60
canvas.size = X, Y
ox,oy = 0,0
canvas.run(draw)

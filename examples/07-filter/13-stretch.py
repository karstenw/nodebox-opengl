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
        image( stretch(img, dx, dy, radius=0.667, zoom=0.95), x=dx, y=dy )
    else:
        image( stretch(img, dx, dy, radius=0.112, zoom=0.35), x=dx, y=dy )


# Start the application:
canvas.fps  = 60
canvas.size = X, Y
ox,oy = 0,0
canvas.run(draw)

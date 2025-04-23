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
        image( bloom(img, intensity=1.0, amount=1, threshold=0.2))
    else:
        image( bloom(img, intensity=0.5, amount=0.5, threshold=0.5))


# Start the application:
canvas.fps  = 60
canvas.size = X,Y
ox,oy = 0,0
canvas.run(draw)

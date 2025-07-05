from nodeboxgl.graphics import *

import os
if os.path.exists("__DEBUG__"):
    img = Image("grid.png")
else:
    img = Image("creature.png")
X,Y = img.width, img.height

def draw(canvas):
    canvas.clear()
    
    if 0:
        image( fisheye( img,
                        canvas.mouse.relative_x,
                        canvas.mouse.relative_y,
                        radius=canvas.mouse.relative_y,
                        zoom=canvas.mouse.relative_x
                        ) )
    else:
        image( fisheye( img,
                        0.5,0.5,
                        radius=canvas.mouse.relative_y*3,
                        zoom=canvas.mouse.relative_x*3
                        ) )
        
# Start the application:
canvas.fps  = 60
canvas.size = X, Y
ox,oy = 0,0
canvas.run(draw)

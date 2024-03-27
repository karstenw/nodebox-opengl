from nodeboxgl.graphics import *

img = Image("creature.png")
X,Y = img.width, img.height

def draw(canvas):
    canvas.clear()
    
    if canvas.mouse.pressed:
        image( img, filter=blurred(scale=1.0) )
    else:
        image( img, filter=blurred(scale=0.2) )


# Start the application:
canvas.fps  = 60
canvas.size = X, Y
ox,oy = 0,0
canvas.run(draw)

from nodeboxgl.graphics import *

img = Image("creature.png")
X,Y = img.width, img.height

def draw(canvas):
    canvas.clear()
    
    dx = canvas.mouse.x / float(canvas.width)
    dy = canvas.mouse.y / float(canvas.height)
    image( pinch(img, dx, dy, zoom=0.75) )

# Start the application:
canvas.fps  = 60
canvas.size = X, Y
canvas.run(draw)

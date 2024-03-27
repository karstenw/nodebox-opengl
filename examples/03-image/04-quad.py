from nodeboxgl.graphics import *

img = Image("creature.png")

# The image.quad property describes the four-sided polygon 
# on which an image texture is "mounted".
# This is not necessarily a rectangle, the corners can be distorted:
img.quad.dx1 =  200
img.quad.dy1 =  100
img.quad.dx2 =  100
img.quad.dy2 = -100

X,Y = 500,500
x2,y2 = round(X/2), round(Y/2)

# This flushes the image cache, so it is a costly operation.

def draw(canvas):
    img.quad.dx2 = -x2 + canvas.mouse.x 
    img.quad.dy2 = -y2 + canvas.mouse.y 
    canvas.clear()
    image(img)
    
canvas.size = X,Y
canvas.run(draw)

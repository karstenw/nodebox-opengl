from nodeboxgl.graphics import *

img = Image("creature.png")
X,Y = img.width, img.height

def draw(canvas):
    canvas.clear()
    
    dx = canvas.mouse.x / float(canvas.width)
    dy = canvas.mouse.y / float(canvas.height)
    if canvas.mouse.pressed:
        image( glow(img, intensity=1.0, amount=1) )
    else:
        image( img  )


# Start the application:
canvas.fps  = 60
canvas.size = X, Y
ox,oy = 0,0
canvas.run(draw)

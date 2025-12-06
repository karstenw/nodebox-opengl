from nodeboxgl.graphics import *

# A classic NodeBox example (http://nodebox.net/code/index.php/Dendrite).
# It registers the dragged mouse movements,
# and use those to draw wavering lines.
# Thanks to Karsten Wolf.

from random import seed
from math   import sin


lines = []

# seed(0)

def draw(canvas):
    background(0.1, 0.0, 0.1, 0.25)
    nofill()
    stroke(1, 1, 1, 0.2)
    strokewidth(0.5)
    
    # Register mouse movement.
    if canvas.mouse.dragged:
        lines.append((LINETO, canvas.mouse.x, canvas.mouse.y, canvas.frame))
    elif canvas.mouse.pressed:
        lines.append((MOVETO, canvas.mouse.x, canvas.mouse.y, canvas.frame))  

    if len(lines) > 0:
        for i in range(5):
            seed(i) # Lock the seed for smooth animation.
            p = BezierPath()
            for cmd, x, y, atframe in lines:
                d = sin((canvas.frame - atframe) / 5.0) * 5.0 # Play with the numbers.
                x += random(-d, d) 
                y += random(-d, d)
                if cmd == MOVETO:
                    p.moveto(x, y)
                else:
                    p.lineto(x, y)
            try:
                drawpath(p)
            except Exception as err:
                if 0:
                    print("p:",p)
                    print(err)
                    print()

canvas.fps = 40
canvas.size = 900, 700
#canvas.fullscreen = True
canvas.run(draw)

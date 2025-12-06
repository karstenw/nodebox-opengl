from nodeboxgl.graphics import *
print(os.path.basename(__file__))

def draw(canvas):
    canvas.clear()
    
canvas.size = 500, 500
canvas.run(draw)

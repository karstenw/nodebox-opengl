from nodeboxgl.graphics import *
from nodeboxgl.graphics.physics import Vector, Boid, Flock, Obstacle

W,H = 900, 700

inset = 50
FW = W + inset + inset
FH = H + inset + inset

flock = Flock(120, x=-inset, y=-inset, width=FW, height=FH)
flock.sight(80)
  
def draw(canvas):
    canvas.clear()
    flock.update(separation=0.4, cohesion=0.6, alignment=0.1, teleport=True)
    for boid in flock:
        push()
        translate(boid.x, boid.y)
        scale(0.5 + boid.depth)
        rotate(boid.heading)
        arrow(0, 0, 15)
        pop()
  
canvas.size = W, H
canvas.run(draw)

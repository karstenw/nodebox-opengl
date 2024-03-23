from nodeboxgl.graphics import *

txt = Text("So long!\nThanks for all the fish.", 
          # font = "Droid Serif", 
          font = "Herculanum",
      fontsize = 90, 
    fontweight = NORMAL,
    lineheight = 1.2,
          fill = color(0.25))

# Text.style() can be used to style individual characters in the text.
# It takes a start index, a stop index, and optional styling parameters:
txt.style(9, len(txt), fontsize=txt.fontsize/2, fontweight=NORMAL)

def draw(canvas):
    
    canvas.clear()

    x = (canvas.width - textwidth(txt)) / 2
    y = 50
    text(txt, x, y)
    
canvas.size = 900, 500
canvas.run(draw)

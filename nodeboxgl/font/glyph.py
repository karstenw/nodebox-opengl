#=== CHARACTER GLYPH PATHS ===========================================================================
# NodeBox for OpenGL has no direct way of accessing glyph path information.
# This script is to be used in the classic NodeBox for Mac OS X (http://nodebox.net).
# It uses the textpath() command to convert characters to paths,
# and store the paths in a file that can be used by NodeBox for OpenGL as glyph path info.

# Defines the characters to process.
# By default, only standard ASCII characters are converted.
from itertools import chain

import io

# characters = range(32, 127)
characters = list(chain( range(32,127), range(160, 512)))

# Defines which fonts to process.
# By default, only the standard fonts in NodeBox for OpenGL
# are converted (Droid Sans, Droid Sans Mono, Droid Serif, Arial).
fonts = {
    "Droid Sans": {
         "normal" : "DroidSans", # PostScript-name.
           "bold" : "DroidSans-Bold"
    },
    "Droid Sans Mono": {
         "normal" : "DroidSansMono"
    },
    "Droid Serif": {
         "normal" : "DroidSerif",
           "bold" : "DroidSerif-Bold",
         "italic" : "DroidSerif-Italic",
    "bold italic" : "DroidSerif-BoldItalic" 
    },
    "Arial": {
         "normal" : "ArialMT",
           "bold" : "Arial-BoldMT",  
    },
    'Verdana': {'bold': 'Verdana-Bold',
             'bold italic': 'Verdana-BoldItalic',
             'italic': 'Verdana-Italic',
             'normal': 'Verdana'},
    'Monaco': {'normal': 'Monaco'},
    'Menlo': {'bold': 'Menlo-Bold',
           'bold italic': 'Menlo-BoldItalic',
           'italic': 'Menlo-Italic',
           'normal': 'Menlo-Regular'},
    'Herculanum': {'normal': 'Herculanum'},
    # 'Acme': {'normal': 'Acme-Regular'},
    'Gill Sans': {
        'bold': 'GillSans-Bold',
        'bold italic': 'GillSans-BoldItalic',
        'italic': 'GillSans-Italic',
        'light': 'GillSans-Light',
        'light italic': 'GillSans-LightItalic',
        'normal': u'GillSans'},
    'FontAwesome': {'normal': 'FontAwesome'},
    'Futura': {
        'condensed extrabold': 'Futura-CondensedExtraBold',
        'condensed medium': 'Futura-CondensedMedium',
        'medium': 'Futura-Medium',
        'medium italic': 'Futura-MediumItalic'},
    'Lato': {
        'normal': 'Lato-Regular',
        'light': 'Lato-Hairline',
        'bold': 'Lato-Bold',
        'bold italic': 'Lato-BoldItalic',
    },
}
"""
    'Eurostile': {
        'bold': 'Eurostile-Bold',
        'bold condensed': 'Eurostile-BoldCondensed',
        'bold extended': 'Eurostile-BoldExtendedTwo',
        'bold oblique': 'Eurostile-BoldOblique',
        'condensed': 'Eurostile-Condensed',
        'demi': 'Eurostile-Demi',
        'demi oblique': 'Eurostile-DemiOblique',
        'extended': 'Eurostile-ExtendedTwo',
        'normal': 'Eurostile',
        'oblique': 'Eurostile-Oblique'},
}
"""

# How point size is measured (NodeBox for OpenGL uses 96dpi).
dpi = 96

# Measure from the baseline?
baseline = True

#=====================================================================================================

glyphs = {}

commands = {
    0: "moveto", 
    1: "lineto", 
    2: "curveto", 
    3: "close"
}

from AppKit import NSFont
def descent(fontname, fontsize=10):
    return NSFont.fontWithName_size_(fontname, fontsize).descender()
    
for fontname in fonts:
    glyphs[fontname] = {}
    print(fontname)
    for fontweight in fonts[fontname]:
        print("   "+fontweight)
        glyphs[fontname][fontweight] = {}
        # Render the font at a large size so we can round the path points.
        # This saves disk space and decreases the loading time.
        _ctx.font(fonts[fontname][fontweight])
        _ctx.fontsize(1000.0 * dpi / 72)
        _ctx.lineheight(1.0)
        dy = baseline and descent(fontname, _ctx.fontsize()) or 0
        for i in characters:
            # ch = unichr(i)
            ch = chr(i)
            # print( i, ch )
            glyphs[fontname][fontweight][ch] = []
            for pt in _ctx.textpath(ch, 0, 0):
                if pt.cmd == 0:
                    pt = [commands[pt.cmd], int(pt.x), int(pt.y-dy)]
                elif pt.cmd == 1:
                    pt = [commands[pt.cmd], int(pt.x), int(pt.y-dy)]
                elif pt.cmd == 2:
                    pt = [commands[pt.cmd], 
                          int(pt.x), int(pt.y-dy), 
                          int(pt.ctrl1.x), int(pt.ctrl1.y-dy), 
                          int(pt.ctrl2.x), int(pt.ctrl2.y-dy)]
                elif pt.cmd == 3:
                    pt = [commands[pt.cmd]]
                glyphs[fontname][fontweight][ch].append(pt)

import pickle
f = open("glyph.p","wb")
pickle.dump(glyphs, f)
f.close()

#=====================================================================================================
# For testing purposes:

def textpath_from_glyphs(string, x=0, y=0, fontname="Droid Sans", fontweight="normal"):
    glyphs = pickle.load(open("glyph.p", 'rb'))
    p = _ctx.BezierPath()
    f = _ctx.fontsize() / 1000.0 * 72 / dpi
    y += textheight(" ", lineheight()) - textheight(" ", lineheight=1)
    from nodebox.graphics import MOVETO, LINETO, CURVETO, CLOSE
    for ch in string:
        glyph = glyphs[fontname][fontweight][ch]
        for pt in glyph:
            if pt[0] == "moveto":
                p.moveto(x+pt[1]*f, y+pt[2]*f)
            elif pt[0] == "lineto":
                p.lineto(x+pt[1]*f, y+pt[2]*f)
            elif pt[0] == "curveto":
                p.curveto(x+pt[3]*f, y+pt[4]*f, x+pt[5]*f, y+pt[6]*f, x+pt[1]*f, y+pt[2]*f)
            elif pt[0] == "close":
                p.closepath()
        x += _ctx.textwidth(ch)
    return p
textpath_from_glyphs("Hello World!", 100,100 )

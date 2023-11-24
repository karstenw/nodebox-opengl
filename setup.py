import os
from setuptools import setup
from setuptools import find_packages
from setuptools.extension import Extension


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


packages = find_packages()
print("packages:", packages)

desc = read("README.txt")
print("desc:", desc)

# Utility function to read the README file.
# From http://packages.python.org/an_example_pypi_project/setuptools.html.
setup(      name = "nodeboxgl",
         version = "1.8",
     description = "NodeBox for OpenGL (NOGL) is a free, cross-platform library "
                   "for generating 2D animations with Python programming code.",
long_description = desc,
        keywords = "2d graphics sound physics games multimedia",
         license = "BSD",
          author = "Tom De Smedt",
             url = "https://cityinabottle.org/nodebox/",
        packages = packages,
    package_data = {"nodeboxgl.gui": ["theme/*"], "nodeboxgl.font":["glyph.p"]},
install_requires = ["pyglet",],
      py_modules = ["nodeboxgl", "nodeboxgl.graphics", "nodeboxgl.gui", "nodeboxgl.sound", "nodeboxgl.font"],

     ext_modules = [
        Extension("nglbezier",   ["nodeboxgl/ext/nglbezier.c"]),
        Extension("nglgeometry", ["nodeboxgl/ext/nglgeometry.c"]),
        Extension("nglnoise",    ["nodeboxgl/ext/nglnoise.c"])
    ],

     classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Artistic Software",
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

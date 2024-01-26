import os
from setuptools import setup
from setuptools import find_packages
from setuptools.extension import Extension


nglbezier   = Extension("nglbezier",   sources=["nglbezier.c"])
nglgeometry = Extension("nglgeometry", sources=["nglgeometry.c"])
nglnoise    = Extension("nglnoise",    sources=["nglnoise.c"])

setup(
         name = "Nodebox for OpenGL c-extensions",
      version = "1.0",
       author = "Tom De Smedt, Frederik De Bleser",
  description = "Fast C Bezier, geometry and noise math.",
  ext_modules = [nglbezier, nglgeometry, nglnoise]
)

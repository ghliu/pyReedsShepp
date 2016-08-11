from distutils.core import setup, Extension
import os
try:
	from Cython.Distutils import build_ext
except:
	use_cython = False
else:
	use_cython = True

cmdclass = {}
ext_modules = []

sources = []
if use_cython:
	sources = ["reeds_shepp/src/reeds_shepp.cpp", "reeds_shepp/reeds_shepp.pyx"]
	cmdclass.update({ 'build_ext' : build_ext })
else:
	sources = ["reeds_shepp/src/reeds_shepp.cpp", "reeds_shepp/reeds_shepp.cpp"]
	
ext_modules = [
    Extension("reeds_shepp",
        sources = sources,
        language="c++",
        include_dirs = ["reeds_shepp/include"])
    ]

def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    contents = open(path).read()
    return contents

setup( 
	name = "reeds_shepp",
    version      = "0.1.1",
    description  = "Code to calculate analytic Reeds Shepp path",
    long_description = read('README.rst'),
    author       = "Guan-Horng Liu",
    author_email = "guanhorl@andrew.cmu.edu",
    license      = "BSD",
    cmdclass     = cmdclass,
    ext_modules  = ext_modules,
	)

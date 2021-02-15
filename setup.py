import setuptools
from Cython.Build import cythonize

# python3 setup.py build_ext --inplace

setuptools.setup(
    name='rirgen',
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    ext_modules=cythonize([
        'rirgen/pyrirgen.pyx'
    ], annotate=True)

)

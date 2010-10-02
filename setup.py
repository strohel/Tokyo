#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

ext_params = {}
ext_params['include_dirs'] = [np.get_include()]
ext_params['extra_compile_args'] = ["-O2"]
ext_params['extra_link_args'] = ["-Wl,-O1", "-Wl,--as-needed"]  # TODO: ad-neeeded ignored

ext_modules=[
    Extension("tokyo", ["tokyo.pyx"], libraries=['cblas', 'lapack'], **ext_params),
    Extension("verify", ["verify.pyx"], **ext_params),
    Extension("single_speed", ["single_speed.pyx"], **ext_params),
    Extension("double_speed", ["double_speed.pyx"], **ext_params),
    Extension("demo_outer", ["demo_outer.pyx"], **ext_params)
]

setup(
#  name = 'BLAS and LAPACK wrapper',
  name = 'BLAS wrapper',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
)

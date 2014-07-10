#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Extension
from autogen import Autogen

setup(
    name='admesh',
    version='0.0.0dev',
    description='Python bindings for admesh, STL maipulation library',
    keywords='STL, mesh, 3D',
    author='Miro Hrončok',
    author_email='miro@hroncok.cz',
    url='https://github.com/hroncok/python_admesh',
    license='GPLv2+',
    packages=find_packages(),
    cmdclass={'build_ext': Autogen},
    ext_modules=[Extension("admesh", ["admesh.pyx"], libraries=["admesh"])]
)

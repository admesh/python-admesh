#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Extension
from autogen import Autogen

long_description = ''.join(open('README.rst').readlines())

setup(
    name='admesh',
    version='0.98a1',
    description='Python bindings for ADMesh, STL maipulation library',
    long_description=long_description,
    keywords='STL, mesh, 3D',
    author='Miro Hrončok',
    author_email='miro@hroncok.cz',
    url='https://github.com/hroncok/python_admesh',
    license='GPLv2+',
    packages=find_packages(),
    cmdclass={'build_ext': Autogen},
    ext_modules=[Extension("admesh", ["admesh.pyx"], libraries=["admesh"])],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                 'Operating System :: POSIX :: Linux',
                 'Operating System :: MacOS :: MacOS X',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 3',
                 'Topic :: Multimedia :: Graphics :: 3D Modeling',
                ],
)

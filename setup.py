#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Extension
from autogen import Autogen

long_description = ''.join(open('README.rst').readlines())

setup(
    name='admesh',
    version='0.98.4',
    description='Python bindings for ADMesh, STL maipulation library',
    long_description=long_description,
    keywords='STL, mesh, 3D',
    author='Miro Hrončok',
    author_email='miro@hroncok.cz',
    url='https://github.com/admesh/python-admesh',
    license='GPLv2+',
    install_requires=['Cython'],
    packages=find_packages(),
    cmdclass={'build_ext': Autogen},
    ext_modules=[Extension("admesh", ["admesh.pyx"], libraries=["admesh"])],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Manufacturing',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Cython',
                 'Programming Language :: Python :: Implementation :: CPython',
                 'Programming Language :: Python :: Implementation :: PyPy',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Topic :: Multimedia :: Graphics :: 3D Modeling',
                 ],
)

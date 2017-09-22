#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
from setuptools import setup, Extension


def _autogen(*args, **kwargs):
    from autogen import Autogen
    return Autogen(*args, **kwargs)


long_description = ''.join(open('README.rst').readlines())
ext_kwargs = {}


if platform.system().startswith('Windows'):
    ext_kwargs['include_dirs'] = ['windows/admesh/include/']
    ext_kwargs['library_dirs'] = ['windows/admesh/lib/']
    ext_kwargs['libraries'] = ['libadmesh']
else:
    ext_kwargs['libraries'] = ['admesh']


setup(
    name='admesh',
    version='0.98.8',
    description='Python bindings for ADMesh, STL maipulation library',
    long_description=long_description,
    keywords='STL, mesh, 3D',
    author='Miro Hrončok',
    author_email='miro@hroncok.cz',
    url='https://github.com/admesh/python-admesh',
    license='GPLv2+',
    setup_requires=['Cython>=0.22', 'pytest-runner'],
    tests_require=['pytest'],
    cmdclass={'build_ext': _autogen},
    ext_modules=[Extension('admesh', ['admesh.pyx'], **ext_kwargs)],
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
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Multimedia :: Graphics :: 3D Modeling',
                 ],
)

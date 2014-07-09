#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext
import subprocess

class Autogen(build_ext, object):
    def run(self, *args, **kwargs):

        NAME = 'admesh'
        HEADERS = [
            '/usr/include/admesh/stl.h',
        ]
        PREFIX = 'stl_'
        PRECUT = len(PREFIX)
        PXD_IGNORE = [
            '',
            'exit_on_error',
            'stats_out',
            'print_neighbors',
            'print_edges',
            'scale_versor',
            'add_facet',
            'allocate',
            'reallocate',
            'count_facets',
        ]
        PYX_IGNORE = ['open', 'close', 'get_error', 'clear_error']

        PXD = 'c' + NAME + '.pxd'
        _PXD = '_' + PXD
        PYX = NAME + '.pyx'
        _PYX = '_' + PYX

        SELF = 'stl_file *stl'

        pxdlines = []
        pyxlines = []

        for header in HEADERS:
            with open(header) as h:
                lines = h.readlines()
            for line in lines:
                if not line:
                    continue
                line = line[:-2] # cut off ;
                line = line.split()
                if not line or line[0] != 'extern':
                    continue
                pxd_line = '    ' + ' '.join(line[1:]) + '\n' # void stl_foo(...)
                line = ' '.join(line[2:]) # stl_foo(...)
                line = line.split('(')
                function = line[0][PRECUT:]
                if function in PXD_IGNORE:
                    continue
                pxdlines.append(pxd_line)
                if function in PYX_IGNORE:
                    continue
                line = line[1][:-1]
                line = [l.strip() for l in line.split(',')]
                static = True
                if line[0] == SELF:
                    static = False
                    line = line[1:]
                if static:
                    continue # this is a hack, we don' want any static method NOW
                args = []
                for arg in line:
                    arg = arg.split()[-1]
                    if arg.startswith('*'):
                        arg = arg[1:]
                    if arg.endswith('[]'):
                        arg = arg[:-2]
                    if arg.endswith('[3]'):
                        arg = arg[:-3]
                    args.append(arg)
                if static:
                    pyxlines.append('    @classmethod\n')
                pyxlines.append('    def ')
                pyxlines.append(function)
                pyxlines.append('(')
                if static:
                    pyxlines.append('cls')
                else:
                    pyxlines.append('self')
                if args:
                    pyxlines.append(', ')
                    label = -1
                    for i, arg in enumerate(args):
                        if arg == 'label':
                            label = i
                    if label >= 0:
                        largs = args[:label] + args[label+1:] + ["label='admesh'"]
                    else:
                        largs = args
                    pyxlines.append(', '.join(largs))
                pyxlines.append('):')
                pyxlines.append('\n        ')
                pyxlines.append(PREFIX+function)
                pyxlines.append('(')
                if not static:
                    pyxlines.append('&self._c_stl_file')
                    if args:
                        pyxlines.append(', ')
                if args:
                    pyxlines.append(', '.join(args))
                pyxlines.append(')\n')
                pyxlines.append('        if stl_get_error(&self._c_stl_file):\n')
                pyxlines.append('            stl_clear_error(&self._c_stl_file)\n')
                pyxlines.append('            raise AdmeshError(\'')
                pyxlines.append(PREFIX+function)
                pyxlines.append('\')\n')
                pyxlines.append('\n')
                

        with open(_PXD, 'r') as _pxd:
            _pxdlines = _pxd.readlines() + ['\n']

        with open(PXD, 'w') as pxd:
            pxd.write(''.join(_pxdlines + pxdlines))
            pxd.write('\n')

        with open(_PYX, 'r') as _pyx:
            _pyxlines = _pyx.readlines() + ['\n']

        with open(PYX, 'w') as pyx:
            pyx.write(''.join(_pyxlines + pyxlines))
            pyx.write('\n')

        super(Autogen, self).run(*args, **kwargs)

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

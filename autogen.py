from __future__ import print_function
from Cython.Distutils import build_ext
import subprocess
import os
import sys


class Autogen(build_ext, object):
    def run(self, *args, **kwargs):
        self.autogen()
        super(Autogen, self).run(*args, **kwargs)

    def autogen(self):
        NAME = 'admesh'
        HEADERS = [
            'admesh/stl.h',
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
            'write_binary_block',
            'put_little_int',
            'put_little_float',
        ]
        PYX_IGNORE = ['open', 'close', 'get_error', 'clear_error', 'repair']

        PXD = 'c' + NAME + '.pxd'
        _PXD = '_' + PXD
        PYX = NAME + '.pyx'
        _PYX = '_' + PYX

        SELF = 'stl_file *stl'

        print('generating {PXD} and {PYX}'.format(PXD=PXD, PYX=PYX))

        pxdlines = []
        pyxlines = []

        for header in HEADERS:
            _header = self.get_header(header)
            if not _header:
                sys.stderr.write('Error: {h} not found, install ADMesh first.\n\nSee README.rst'
                                 'for more information\n'.format(h=header))
                exit(1)
            with open(_header) as h:
                lines = h.readlines()
            for line in lines:
                if not line:
                    continue
                line = line[:-2]  # cut off ;
                line = line.split()
                if not line or line[0] != 'extern':
                    continue
                pxd_line = '    ' + ' '.join(line[1:]) + '\n'  # void stl_foo(...)
                line = ' '.join(line[2:])  # stl_foo(...)
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
                    continue  # this is a hack, we don' want any static method NOW
                args = []
                chars = set()
                for arg in line:
                    char = arg.split()[-2]
                    arg = arg.split()[-1]
                    if arg.startswith('*'):
                        arg = arg[1:]
                    if arg.endswith('[]'):
                        arg = arg[:-2]
                    if arg.endswith('[3]'):
                        arg = arg[:-3]
                    args.append(arg)
                    if char == 'char':
                        chars.add(arg)
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
                pyxlines.append('\n        """')
                pyxlines.append(PREFIX+function)
                pyxlines.append('"""')
                pyxlines.append('\n        if not self._opened:')
                pyxlines.append('\n            raise AdmeshError(\'STL not opened\')')
                for idx, arg in enumerate(args):
                    if arg not in chars:
                        continue
                    pyxlines.append('\n        ')
                    pyxlines.append('by_{arg} = {arg}.encode(\'UTF-8\')'.format(arg=arg))
                    args[idx] = 'by_' + arg
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

        with open(_PYX, 'r') as _pyx:
            _pyxlines = _pyx.readlines() + ['\n']

        with open(PYX, 'w') as pyx:
            pyx.write(''.join(_pyxlines + pyxlines))

    def get_header(self, header):
        cflags = os.environ.get('CFLAGS', '')
        p = subprocess.Popen('gcc -v -E -'.split() + cflags.split(), stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, log = p.communicate('')
        log = log.decode('utf8').split('\n')
        read = False
        for line in log:
            if 'search starts here:' in line:
                read = True
                continue
            if 'End of search list' in line:
                break
            if read:
                candidate = os.path.join(line.strip(), header)
                if os.path.isfile(candidate):
                    print("found %s" % candidate)
                    return candidate
        return None

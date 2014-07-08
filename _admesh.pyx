from cadmesh cimport *


class Trap:
    def __init__(self):
        self.log = []

    def write(self, data):
        self.log.append(data)

class AdmeshError(Exception):
    pass


cdef class Stl:
    cdef stl_file _c_stl_file
    cdef bint _opened
    def __cinit__(self, path=''):
        self._opened = False
        if path:
            self.open(path)

    def open(self, path):
        stl_open(&self._c_stl_file, path)
        if stl_get_error(&self._c_stl_file):
            stl_clear_error(&self._c_stl_file)
            raise AdmeshError('stl_open')
        self._opened = True

    def __dealloc__(self):
        if self._opened:
            stl_close(&self._c_stl_file)

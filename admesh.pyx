from cadmesh cimport *
from libc.stdlib cimport malloc, free
import sys

class Trap:
    def __init__(self):
        self.log = []

    def write(self, data):
        self.log.append(data)

cdef class Stl:
    cdef stl_file* _c_stl_file
    cdef bint _opened
    def __cinit__(self):
        self._c_stl_file = <stl_file*> malloc(sizeof(stl_file))
        if self._c_stl_file is NULL:
            raise MemoryError()
        self._opened = False

    def open(self, path):
        stl_open(self._c_stl_file, path)
        self._opened = True

    def __dealloc__(self):
        if self._opened:
            stl_close(self._c_stl_file)
            self._opened = False
        if self._c_stl_file is not NULL:
            free(self._c_stl_file)

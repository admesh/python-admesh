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
            raise AdmeshError('Could not open STL {path}'.format(path=path))
        self._opened = True

    def write_binary(self, path, label='admesh'):
        stl_write_binary(&self._c_stl_file, path, label)
        if stl_get_error(&self._c_stl_file):
            raise AdmeshError('Could not save binary STL {path}'.format(path=path))


    def write_ascii(self, path, label='admesh'):
        stl_write_ascii(&self._c_stl_file, path, label)
        if stl_get_error(&self._c_stl_file):
            raise AdmeshError('Could not save ASCII STL {path}'.format(path=path))

    def __dealloc__(self):
        if self._opened:
            stl_close(&self._c_stl_file)

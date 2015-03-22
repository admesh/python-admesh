from cadmesh cimport *


class AdmeshError(Exception):
    pass


cdef class Stl:
    cdef stl_file _c_stl_file
    cdef bint _opened

    BINARY = 0
    ASCII = 1
    INMEMORY = 2

    def __cinit__(self, path=''):
        self._opened = False
        if path:
            self.open(path)

    def get_stats(self):
        return self._c_stl_file.stats

    stats = property(lambda self: self.get_stats())

    def open(self, path):
        """stl_open"""
        by_path = path.encode('UTF-8')
        stl_open(&self._c_stl_file, by_path)
        if stl_get_error(&self._c_stl_file):
            stl_clear_error(&self._c_stl_file)
            raise AdmeshError('stl_open')
        self._opened = True

    def repair(self,
               fixall_flag=True,
               exact_flag=False,
               tolerance_flag=False,
               tolerance=0,
               increment_flag=False,
               increment=0,
               nearby_flag=False,
               iterations=2,
               remove_unconnected_flag=False,
               fill_holes_flag=False,
               normal_directions_flag=False,
               normal_values_flag=False,
               reverse_all_flag=False,
               verbose_flag=True):
        """stl_repair"""
        if not self._opened:
            raise AdmeshError('STL not opened')
        stl_repair(&self._c_stl_file,
                   fixall_flag,
                   exact_flag,
                   tolerance_flag,
                   tolerance,
                   increment_flag,
                   increment,
                   nearby_flag,
                   iterations,
                   remove_unconnected_flag,
                   fill_holes_flag,
                   normal_directions_flag,
                   normal_values_flag,
                   reverse_all_flag,
                   verbose_flag)
        if stl_get_error(&self._c_stl_file):
            stl_clear_error(&self._c_stl_file)
            raise AdmeshError('stl_repair')


    def __dealloc__(self):
        if self._opened:
            stl_close(&self._c_stl_file)

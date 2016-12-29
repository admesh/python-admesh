from cadmesh cimport *

class AdmeshError(Exception):
    pass


cdef class Stl(object):
    cdef stl_file _c_stl_file
    cdef bint _opened
    cdef int _iterindex

    BINARY = 0
    ASCII = 1
    INMEMORY = 2

    def __cinit__(self, path=''):
        if path:
            self._open(path)
        else:
            stl_initialize(&self._c_stl_file)
            if stl_get_error(&self._c_stl_file):
                stl_clear_error(&self._c_stl_file)
                raise AdmeshError('stl_initialize')
            self._c_stl_file.stats.type = Stl.INMEMORY

    property stats:
        """The statistics about the STL model"""
        def __get__(self):
            return self._c_stl_file.stats

    def __str__(self):
        header = str(self._c_stl_file.stats.header.decode('ascii'))
        if self._c_stl_file.stats.type == Stl.ASCII and header.startswith('solid '):
            header = header[len('solid '):].strip()
        return 'Stl(\'{header}\')'.format(header=header)

    def __iter__(self):
        self._iterindex = 0
        return self

    def __next__(self):
        if self._iterindex >= len(self):
            raise StopIteration
        self._iterindex += 1
        return self._c_stl_file.facet_start[self._iterindex - 1]

    def __len__(self):
        return self._c_stl_file.stats.number_of_facets

    def _open(self, path):
        by_path = path.encode('UTF-8')
        stl_open(&self._c_stl_file, by_path)
        if stl_get_error(&self._c_stl_file):
            stl_clear_error(&self._c_stl_file)
            raise AdmeshError('stl_open')

    def add_facets(self, facets):
        """
        Add one or more facets

        every facet is a tuple of two elements:
            * vertices: tuple of three points (each a tuple of three floats)
            * normal: tuple of three floats

        Example usage:
            stl_object.add_facets([
                (((0, 0, 0), (1, 0, 0), (0, 1, 0)), (1, 0, 0)),
                (((0, 0, 0), (0, 1, 0), (1, 0, 0)), (0, 1, 0)),
            ])
        """
        cdef stl_facet facet_struct
        cdef size_t i
        current_facet_index = self._c_stl_file.stats.number_of_facets
        self._c_stl_file.stats.number_of_facets += len(facets)
        stl_reallocate(&self._c_stl_file)
        if stl_get_error(&self._c_stl_file):
            # reset the facet count back to the original size
            self._c_stl_file.stats.number_of_facets = current_facet_index
            stl_clear_error(&self._c_stl_file)
            raise AdmeshError('stl_reallocate')
        for facet in facets:
            for i in range(3):
                facet_struct.vertex[i] = stl_vertex(facet[0][i][0],
                                                    facet[0][i][1],
                                                    facet[0][i][2])
            facet_struct.normal = stl_normal(facet[1][0],
                                             facet[1][1],
                                             facet[1][2])
            self._c_stl_file.facet_start[current_facet_index] = facet_struct
            stl_facet_stats(&self._c_stl_file, facet_struct, False);
            current_facet_index += 1

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
        stl_close(&self._c_stl_file)

cdef extern from "admesh/stl.h":
    ctypedef struct stl_vertex:
        pass

    ctypedef struct stl_normal:
        pass

    ctypedef struct stl_facet:
        pass

    cdef enum stl_type:
        pass

    ctypedef struct stl_edge:
        pass

    ctypedef struct stl_hash_edge:
        pass

    ctypedef struct stl_neighbors:
        pass

    ctypedef struct v_indices_struct:
        pass

    ctypedef struct stl_stats:
        pass

    ctypedef struct stl_file:
        pass

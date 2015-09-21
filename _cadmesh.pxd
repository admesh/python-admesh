cdef extern from "admesh/stl.h":
    ctypedef struct stl_vertex:
        float x
        float y
        float z

    ctypedef struct stl_normal:
        float x
        float y
        float z

    ctypedef char stl_extra[2]

    ctypedef struct stl_facet:
        stl_normal normal
        stl_vertex vertex[3]
        stl_extra  extra

    ctypedef enum stl_type:
        binary, ascii, inmemory

    ctypedef struct stl_edge:
        pass

    ctypedef struct stl_hash_edge:
        pass

    ctypedef struct stl_neighbors:
        pass

    ctypedef struct v_indices_struct:
        pass

    ctypedef struct stl_stats:
        char          header[81]
        stl_type      type
        int           number_of_facets
        stl_vertex    max
        stl_vertex    min
        stl_vertex    size
        float         bounding_diameter
        float         shortest_edge
        float         volume
        unsigned      number_of_blocks
        int           connected_edges
        int           connected_facets_1_edge
        int           connected_facets_2_edge
        int           connected_facets_3_edge
        int           facets_w_1_bad_edge
        int           facets_w_2_bad_edge
        int           facets_w_3_bad_edge
        int           original_num_facets
        int           edges_fixed
        int           degenerate_facets
        int           facets_removed
        int           facets_added
        int           facets_reversed
        int           backwards_edges
        int           normals_fixed
        int           number_of_parts
        int           malloced
        int           freed
        int           facets_malloced
        int           collisions
        int           shared_vertices
        int           shared_malloced

    ctypedef struct stl_file:
        stl_stats     stats
        stl_facet     *facet_start

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

    void stl_open(stl_file *stl, char *file)
    void stl_close(stl_file *stl)
    void stl_print_neighbors(stl_file *stl, char *file)
    void stl_write_ascii(stl_file *stl, const char *file, const char *label)
    void stl_write_binary(stl_file *stl, const char *file, const char *label)
    void stl_check_facets_exact(stl_file *stl)
    void stl_check_facets_nearby(stl_file *stl, float tolerance)
    void stl_remove_unconnected_facets(stl_file *stl)
    void stl_write_vertex(stl_file *stl, int facet, int vertex)
    void stl_write_facet(stl_file *stl, char *label, int facet)
    void stl_write_edge(stl_file *stl, char *label, stl_hash_edge edge)
    void stl_write_neighbor(stl_file *stl, int facet)
    void stl_write_quad_object(stl_file *stl, char *file)
    void stl_verify_neighbors(stl_file *stl)
    void stl_fill_holes(stl_file *stl)
    void stl_fix_normal_directions(stl_file *stl)
    void stl_fix_normal_values(stl_file *stl)
    void stl_reverse_all_facets(stl_file *stl)
    void stl_translate(stl_file *stl, float x, float y, float z)
    void stl_translate_relative(stl_file *stl, float x, float y, float z)
    void stl_scale_versor(stl_file *stl, float versor[3])
    void stl_scale(stl_file *stl, float factor)
    void stl_rotate_x(stl_file *stl, float angle)
    void stl_rotate_y(stl_file *stl, float angle)
    void stl_rotate_z(stl_file *stl, float angle)
    void stl_mirror_xy(stl_file *stl)
    void stl_mirror_yz(stl_file *stl)
    void stl_mirror_xz(stl_file *stl)
    void stl_open_merge(stl_file *stl, char *file)
    void stl_invalidate_shared_vertices(stl_file *stl)
    void stl_generate_shared_vertices(stl_file *stl)
    void stl_write_obj(stl_file *stl, char *file)
    void stl_write_off(stl_file *stl, char *file)
    void stl_write_dxf(stl_file *stl, char *file, char *label)
    void stl_write_vrml(stl_file *stl, char *file)
    void stl_calculate_normal(float normal[], stl_facet *facet)
    void stl_normalize_vector(float v[])
    void stl_calculate_volume(stl_file *stl)
    void stl_initialize(stl_file *stl)
    void stl_count_facets(stl_file *stl, char *file)
    void stl_allocate(stl_file *stl)
    void stl_read(stl_file *stl, int first_facet, int first)
    void stl_facet_stats(stl_file *stl, stl_facet facet, int first)
    void stl_reallocate(stl_file *stl)
    void stl_get_size(stl_file *stl)

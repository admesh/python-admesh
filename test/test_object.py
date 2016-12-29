# -*- coding: utf-8 -*-
from admesh import Stl


class TestObjectCapabilities(object):
    '''Tests object capabilities'''
    def test_len_is_number_of_facets(self):
        '''Tests if len() of Stl object is number of factes'''
        stl = Stl('test/block.stl')
        assert len(stl) == 12

    def test_list_from_stl(self):
        '''Tests if list(stl) returns all the facets'''
        stl = Stl('test/block.stl')
        facets = list(stl)
        assert len(facets) == 12
        assert len(facets[0]['vertex']) == 3
        assert facets[0]['vertex'][0]['x'] == 0

    def test_add_facets(self):
        stl = Stl('test/block.stl')
        facet_count = len(stl)
        stl.add_facets([(((0, 0, 0), (1, 1, 1), (1, 0, 0)), (1, 0, 0))])
        assert len(stl) == facet_count + 1

    def test_str(self):
        '''Tests the output of str'''
        stl = Stl('test/block.stl')
        assert str(stl) == "Stl('admesh')"

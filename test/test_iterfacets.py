# -*- coding: utf-8 -*-
from admesh import Stl


class TestIterFacets(object):
    '''Tests that we can iterate over factes'''
    def test_len_is_number_of_facets(self):
        '''Tests if len() of Stl object is number_of_factes'''
        stl = Stl('test/block.stl')
        assert len(stl) == 12

    def test_list_from_stl(self):
        '''Tests if list(stl) returns all the facets'''
        stl = Stl('test/block.stl')
        facets = list(stl)
        assert len(facets) == 12
        assert len(facets[0]['vertex']) == 3
        assert facets[0]['vertex'][0]['x'] + 1.96850395 < 0.0000001

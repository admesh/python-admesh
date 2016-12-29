# -*- coding: utf-8 -*-
import sys
import pytest
from admesh import Stl


pypy2 = '__pypy__' in sys.builtin_module_names and sys.version_info.major == 2


class TestStats(object):
    '''Tests that stats are propagated'''
    def test_number_of_facets(self):
        '''Tests if block has 12 facets'''
        stl = Stl('test/block.stl')
        assert stl.stats['number_of_facets'] == 12

    def test_volume(self):
        '''Tests the volume of the block'''
        stl = Stl('test/block.stl')
        stl.calculate_volume()
        assert stl.stats['volume'] == 1

    def test_header(self):
        '''Tests the header of the block'''
        stl = Stl('test/block.stl')
        assert stl.stats['header'] == 'solid  admesh'.encode('UTF-8')

    def test_add_facets_updates_stats(self):
        '''Tests if adding new facets updates the mesh stats'''
        stl = Stl('test/block.stl')
        max_x = stl.stats['max']['x']
        bounding_diameter = stl.stats['bounding_diameter']
        stl.add_facets([(((0, 0, 0), (1, 1, 1), (max_x + 1, 0, 0)), (1, 0, 0))])
        assert max_x + 1 == stl.stats['max']['x']
        assert bounding_diameter < stl.stats['bounding_diameter']

    def test_write_to_stats(self):
        '''Test if writing to stats raises exception'''
        stl = Stl()
        with pytest.raises(TypeError if pypy2 else AttributeError):
            stl.stats = {}

    def test_delete_stats(self):
        '''Test if deleting stats raises exception'''
        stl = Stl()
        with pytest.raises(AttributeError):
            del stl.stats

# -*- coding: utf-8 -*-
import sys
import pytest
from admesh import Stl
from utils import asset


pypy2 = '__pypy__' in sys.builtin_module_names and sys.version_info.major == 2


class TestStats(object):
    '''Tests that stats are propagated'''
    def test_number_of_facets(self):
        '''Tests if block has 12 facets'''
        stl = Stl(asset('block.stl'))
        assert stl.stats['number_of_facets'] == 12

    def test_volume(self):
        '''Tests the volume of the block'''
        stl = Stl(asset('block.stl'))
        stl.calculate_volume()
        assert stl.stats['volume'] == 1

    def test_header(self):
        '''Tests the header of the block'''
        stl = Stl(asset('block.stl'))
        assert stl.stats['header'] == 'solid  admesh'.encode('UTF-8')

    def test_add_facets_updates_stats(self):
        '''Tests if adding new facets updates the mesh stats'''
        stl = Stl(asset('block.stl'))
        max_x = stl.stats['max']['x']
        bounding_diameter = stl.stats['bounding_diameter']
        stl.add_facets([(((0, 0, 0), (1, 1, 1), (max_x + 1, 0, 0)), (1, 0, 0))])
        assert max_x + 1 == stl.stats['max']['x']
        assert bounding_diameter < stl.stats['bounding_diameter']

    @pytest.mark.parametrize('type', ('iterable', 'dict'))
    def test_stats_are_same_with_created(self, type):
        ''''Test a manually constructed cube has the same stats as if loaded'''
        XYZ = ('x', 'y', 'z')
        stl1 = Stl(asset('block.stl'))
        if type == 'iterable':
            facets = [[[[v[a] for a in XYZ] for v in f['vertex']],
                       [f['normal'][a] for a in XYZ]] for f in stl1]
        else:
            facets = list(stl1)
        stl2 = Stl()
        stl2.add_facets(facets)
        stats1, stats2 = stl1.stats, stl2.stats
        for stats in (stats1, stats2):
            del stats['type']  # ASCII != INMEMORY
            del stats['original_num_facets']  # 12 != 0
            del stats['header']  # nothing != "solid  admesh"
        assert stats1 == stats2

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

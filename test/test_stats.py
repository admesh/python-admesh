# -*- coding: utf-8 -*-
from admesh import Stl


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
        assert stl.stats['volume'] > 61
        assert stl.stats['volume'] < 62

    def test_header(self):
        '''Tests the header of the block'''
        stl = Stl('test/block.stl')
        assert stl.stats['header'] == 'solid  admesh'.encode('UTF-8')

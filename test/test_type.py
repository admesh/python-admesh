# -*- coding: utf-8 -*-
from admesh import Stl


class TestType(object):
    '''Tests for the type recognition'''
    def test_ascii_is_ascii(self):
        '''Tests if loaded ASCII file is recognized as ASCII'''
        stl = Stl('test/block.stl')
        assert stl.stats['type'] == Stl.ASCII

    def test_saved_binary_is_binary(self):
        '''Tests if saved binary file is identical to the loaded one'''
        stl1 = Stl('test/block.stl')
        stl1.write_binary('test/block_binary.stl')
        stl2 = Stl('test/block_binary.stl')
        assert stl2.stats['type'] == Stl.BINARY

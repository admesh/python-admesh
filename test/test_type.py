# -*- coding: utf-8 -*-
from admesh import Stl
from utils import asset


class TestType(object):
    '''Tests for the type recognition'''
    def test_ascii_is_ascii(self):
        '''Tests if loaded ASCII file is recognized as ASCII'''
        stl = Stl(asset('block.stl'))
        assert stl.stats['type'] == Stl.ASCII

    def test_saved_binary_is_binary(self):
        '''Tests if saved binary file is identical to the loaded one'''
        stl1 = Stl(asset('block.stl'))
        stl1.write_binary(asset('block_binary.stl'))
        stl2 = Stl(asset('block_binary.stl'))
        assert stl2.stats['type'] == Stl.BINARY

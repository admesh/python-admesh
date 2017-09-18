# -*- coding: utf-8 -*-
from admesh import Stl
from utils import asset
import filecmp


class TestIO(object):
    '''Tests for the  basic IO operations'''
    def test_saved_equals_original_ascii(self):
        '''Tests if saved ASCII file is identical to the loaded one'''
        stl = Stl(asset('block.stl'))
        stl.write_ascii(asset('block_ascii.stl'))
        assert filecmp.cmp(asset('block.stl'), asset('block_ascii.stl'))

    def test_saved_equals_original_binary(self):
        '''Tests if saved binary file is identical to the loaded one'''
        stl1 = Stl(asset('block.stl'))
        stl1.write_binary(asset('block_binary.stl'))
        stl2 = Stl(asset('block_binary.stl'))
        stl2.write_binary(asset('block_binary2.stl'))
        assert filecmp.cmp(asset('block_binary.stl'), asset('block_binary2.stl'))

    def test_save_load_unicode(self):
        '''Tests saving and loading files with Unicode filenames'''
        stl1 = Stl(asset('block.stl'))
        stl1.write_ascii(asset(u'block_ěščřž.stl'))
        stl2 = Stl(asset(u'block_ěščřž.stl'))

# -*- coding: utf-8 -*-
from admesh import Stl
import filecmp


class TestIO(object):
    '''Tests for the  basic IO operations'''
    def test_saved_equals_original_ascii(self):
        '''Tests if saved ASCII file is identical to the loaded one'''
        stl = Stl('test/block.stl')
        stl.write_ascii('test/block_ascii.stl')
        assert filecmp.cmp('test/block.stl', 'test/block_ascii.stl')

    def test_saved_equals_original_binary(self):
        '''Tests if saved binary file is identical to the loaded one'''
        stl1 = Stl('test/block.stl')
        stl1.write_binary('test/block_binary.stl')
        stl2 = Stl('test/block_binary.stl')
        stl2.write_binary('test/block_binary2.stl')
        assert filecmp.cmp('test/block_binary.stl', 'test/block_binary2.stl')

    def test_save_load_unicode(self):
        '''Tests saving and loading files with Unicode filenames'''
        stl1 = Stl('test/block.stl')
        stl1.write_ascii(u'test/block_ěščřž.stl')
        stl2 = Stl(u'test/block_ěščřž.stl')

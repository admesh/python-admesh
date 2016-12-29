# -*- coding: utf-8 -*-
from admesh import Stl

import pytest


def test_open_is_deprecated():
    s = Stl()
    with pytest.warns(DeprecationWarning):
        s.open('test/block.stl')

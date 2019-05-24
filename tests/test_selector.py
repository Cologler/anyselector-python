# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from anyselector.selector import attr, item

def test_select_attr():
    class C:
        val = 15

    assert attr('val')(C()) == 15

def test_select_item():
    d = {'x': 44}

    assert item('x')(d) == 44

# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from anyselector.selector import attr, item, const

def test_select_attr():
    class C:
        val = 15

    assert attr('val')(C()) == 15

def test_select_item():
    d = {'x': 44}

    assert item('x')(d) == 44

def test_select_const():
    a = 15

    assert const(a)(*(), **{}) is a

def test_select_then_call_with():
    def func(a, b):
        return a, b

    assert const(func).call_with(1, 2)(*(), **{}) == (1, 2)

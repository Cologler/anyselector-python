# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from anyselector.argselector import self, arg, kwarg

def test_select_self():
    assert self()(1) == 1

def test_select_arg():
    assert arg(3)(1, 2, 3, 4) == 4

def test_select_kwarg():
    assert kwarg('k')(k=15) == 15

def test_select_then_attr():
    class C:
        val = 15

    assert self().attr('val')(C()) == 15

def test_select_then_item():
    d = {'x': 44}

    assert self().item('x')(d) == 44

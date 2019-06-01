# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from .selector import Selector

def arg(index):
    '''
    select by index from args.
    '''

    return Selector(
        lambda *args, **kwargs: args[index]
    )

def kwarg(key):
    '''
    select by key from kwargs.
    '''

    return Selector(
        lambda *args, **kwargs: kwargs[key]
    )

def self():
    '''
    select `self` from function args.

    equals `arg(0)`.
    '''
    return arg(0)

# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

class Selector:
    __slots__ = ('_select_func', )

    def __init__(self, select_func):
        self._select_func = select_func

    def select(self, *args, **kwargs):
        '''
        select value.
        '''
        return self._select_func(*args, **kwargs)

    __call__ = select

    def attr(self, name):
        '''
        then select by getattr.
        '''

        return Selector(
            lambda *args, **kwargs:
            getattr(self._select_func(*args, **kwargs), name)
        )

    def item(self, index):
        '''
        then select by getitem.
        '''

        return Selector(
            lambda *args, **kwargs:
            self._select_func(*args, **kwargs)[index]
        )

    def call_with(self, *args, **kwargs):
        '''
        then select by `__call__(*args, **kwargs)`.
        '''

        return Selector(
            lambda *args_, **kwargs_:
            self._select_func(*args_, **kwargs_)(*args, **kwargs)
        )


def _ensure_single_args(*args, **kwargs):
    if kwargs:
        raise ValueError
    if len(args) != 1:
        raise ValueError
    return args[0]

_single_selector = Selector(lambda *args, **kwargs: _ensure_single_args(*args, **kwargs))

def attr(name):
    '''
    select by getattr.

    require single args.
    '''
    return _single_selector.attr(name)

def item(index):
    '''
    select by getitem.

    require single args.
    '''
    return _single_selector.item(index)

def const(value):
    '''
    select by const value.
    '''
    return Selector(lambda *args, **kwargs: value)

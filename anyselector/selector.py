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
        if not isinstance(name, Selector):
            name = const(name)

        return Selector(
            lambda *args, **kwargs:
            getattr(self._select_func(*args, **kwargs), name.select(*args, **kwargs))
        )

    def item(self, index):
        '''
        then select by getitem.
        '''
        if not isinstance(index, Selector):
            index = const(index)

        return Selector(
            lambda *args, **kwargs:
            self._select_func(*args, **kwargs)[index.select(*args, **kwargs)]
        )

    def call_with(self, *args, **kwargs):
        '''
        then select by `__call__(*args, **kwargs)`.
        '''
        args = [x if isinstance(x, Selector) else const(x) for x in args]
        kwargs = dict(
            (k, v) if isinstance(v, Selector) else (k, const(v))
            for k, v in kwargs.items()
        )

        return Selector(
            lambda *args_, **kwargs_:
            self._select_func(*args_, **kwargs_)(
                *[x.select(*args_, **kwargs_) for x in args],
                **dict((k, v.select(*args_, **kwargs_)) for k, v in kwargs.items())
            )
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

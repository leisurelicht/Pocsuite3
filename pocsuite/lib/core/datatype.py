#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import types
import collections

from pocsuite.lib.core.exception import PocsuiteDataException


class AttribDict(collections.UserDict):
    """
    >>> foo = AttribDict()
    >>> foo.bar = 1
    >>> foo.bar
    1
    """

    def __init__(self, indict=None, attribute=None):
        #  __import__('pdb').set_trace()

        if indict is None:
            indict = {}

        self.attribute = attribute
        # 没有用super(AttribDict, self).__setattr__()的写法是因为self会报错
        # 具体原因我也不知道
        super().__init__(indict)
        self.__initialised = True

    def __missing__(self, item):
        raise PocsuiteDataException("unable to access item {}".format(item))

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __setattr__(self, item, value):
        if "_AttribDict__initialised" not in self.__dict__:
            """"""

            return super().__setattr__(item, value)

        elif item in self.__dict__:
            super().__setattr__(item, value)

        else:
            self.__setitem__(item, value)

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self):
        self.__dict__ = dict

    def __deepcopy__(self, memo):
        pass
        # TODO
        # 先不实现了，用到再说吧

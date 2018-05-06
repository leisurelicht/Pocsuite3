#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pocsuite.api.poc import register


class test_class():
    def test_func(self, arg):
        tmp = "hello {}".format(arg)
        print(tmp)

        return tmp


register(test_class)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pocsuite.lib.core.data import kb


def register_poc(poc_class):
    """
    >> test_class.__module__
    >> tests.data_used_to_test

    >> register_poc(test_class)
    >> kb.register_pocs
    >> ['data_userd_to_test']
    """
    module = poc_class.__module__.split('.')[-1]

    if not kb.registered_pocs:
        kb.registered_pocs = {}

    if module in kb.registered_pocs:
        return
    kb.registered_pocs[module] = poc_class()

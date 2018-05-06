#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pocsuite.api.poc import register
from pocsuite.lib.core.data import kb

from tests.data_used_to_test import test_class


class TestRegisterFuction:
    def test_register_poc(self):
        register(test_class)

        assert kb.registered_pocs is not None
        assert test_class.__module__.split('.')[-1] in kb.registered_pocs

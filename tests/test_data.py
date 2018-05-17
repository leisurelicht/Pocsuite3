#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pocsuite.lib.core.data import kb
from pocsuite.lib.core.data import conf
from pocsuite.lib.core.exception import PocsuiteDataException


class TestData():
    def test_conf_not_exists_attr(self):
        with pytest.raises(PocsuiteDataException):
            conf.test

    # def test_conf_not_exists_attr(self):
    #     assert conf.test is None

    def test_conf_attr(self):
        conf.test = 'test'
        assert conf.test == 'test'

    def test_kb_not_exists_attr(self):
        with pytest.raises(PocsuiteDataException):
            kb.test

    # def test_kb_not_exists_attr(self):
    #     assert kb.test is None

    def test_kb_attr(self):
        kb.test = 'test'
        assert kb.test == 'test'

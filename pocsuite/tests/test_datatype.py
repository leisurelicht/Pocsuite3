#!/usr/bin/env python
# -*- coding: utf-8 -*-
import addpath

import pytest
from pocsuite.lib.core.datatype import AttribDict
from pocsuite.lib.core.exception import PocsuiteDataException


class TestAttribDict():
    def setup_class(self):
        self.test1 = AttribDict()
        self.test2 = AttribDict(indict={'a': 1, 'b': 2})
        self.test3 = AttribDict(attribute='test3')

    def test_initialised_be_set(self):
        assert '_AttribDict__initialised' in self.test1.__dict__
        assert '_AttribDict__initialised' in self.test2.__dict__
        assert '_AttribDict__initialised' in self.test3.__dict__
        assert self.test1._AttribDict__initialised
        assert self.test2._AttribDict__initialised
        assert self.test3._AttribDict__initialised

    def test_attr_does_not_exists(self):
        with pytest.raises(PocsuiteDataException):
            self.test1.name

    def test_attr_create_without_param(self):
        self.test1.name = 'test1'
        assert self.test1.name == 'test1'

    def test_attr_create_with_indict(self):
        assert self.test2 == {'a': 1, 'b': 2}
        assert self.test2.a == 1
        assert self.test2.b == 2

    def test_attr_create_with_attribut(self):
        assert self.test3.attribute == 'test3'
        assert 'attribute' in self.test3.__dict__

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest
from pocsuite.lib.core.defaults import POC_IMPORTDICT
from pocsuite.lib.core.common import multiple_replace
from pocsuite.lib.core.common import file_path_parser
from pocsuite.lib.core.common import string_importer
from pocsuite.lib.core.data import conf
from pocsuite.lib.core.data import kb


class TestCommonFunction:
    def test_multiple_replace(self):
        test = '\n'.join(POC_IMPORTDICT.keys())
        result = '\n'.join(POC_IMPORTDICT.values())

        test = multiple_replace(test, POC_IMPORTDICT)
        assert test == result

    def test_file_path_parser(self):
        test = "/tmp/poc/poc_1_0_test.py"
        result = file_path_parser(test)
        assert result == ("/tmp/poc", "poc_1_0_test")

    def test_file_path_parser_only_file(self):
        test = "poc_1_0_test.py"
        result = file_path_parser(test)
        assert result == ("", "poc_1_0_test")

    def test_file_path_parser_only_name(self):
        test = "poc_1_0_test"
        result = file_path_parser(test)
        assert result == ("", "poc_1_0_test")

    def test_file_path_parser_on_win(self):
        """还得装个windows测试"""
        pass


class TestStringImporterFunction:
    def setup_class(self):
        conf.is_pyc_file = False
        self.code = open('tests/data_used_to_test.py').read()

    def test_string_importer_befor_import(self):
        with pytest.raises(ImportError):
            from import_test import test_class

    def test_string_importer(self):
        importer = string_importer('import_test', self.code)
        assert importer == sys.modules['import_test']

    def test_import_attr_after_string_importer(self):
        test_class = getattr(sys.modules['import_test'], 'test_class')
        test = test_class()
        assert test.test_func('test') == 'hello test'

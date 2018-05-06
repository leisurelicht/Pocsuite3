#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import socket
from pocsuite.lib.core.data import kb
from pocusuite.lib.core.data import conf
from pocusuite.lib.core.data import logger
from pocsuite.lib.core.enums import CUSTOM_LOGGING
from pocsuite.lib.core.defaults import POC_IMPORTDICT
from pocsuite.lib.core.defaults import HTTP_DEFAULT_HEADER

from pocsuite.lib.core.common import multiple_replace
from pocsuite.lib.core.common import file_path_parser
from pocsuite.lib.core.common import string_importer
# from pocsuite.lib.core.common import delModule

from pocsuite.lib.core.exception import PocsuiteDataException
from pocsuite.lib.core.exception import PocsuiteValueException


class Cannon():
    """
    导入
    """

    def __init__(self,
                 target,
                 info=None,
                 mode='veirfy',
                 params=None,
                 headers=None,
                 timeout=30):
        self.target = target
        try:
            self.poc_string = info["pocstring"]
            self.poc_name = info["pocname"].replace('.', '')  # 这里为什么要替换掉.?
        except KeyError:
            raise "[X] info must include pocname and pocstring!"
        self.mode = ('verify', 'attack')[mode == 'attack']
        self.params = params or {}

        conf.is_pyc_file = info.get('ispycfile', False)
        conf.http_headers = HTTP_DEFAULT_HEADER

        if headers and isinstance(headers, dict):
            conf.http_headers.update(headers)

        # 把对象不存在时的初始化操作分开放到datatype和第一次访问时去做了
        # try:
        #     kb.registered_pocs
        # except PocsuiteDataException:
        #     kb.registered_pocs = {}

        self._set_http_timeout(timeout)
        self._register_poc()

    def _set_http_timeout(self, timeout):
        socket.setdefaulttimeout(float(timeout))

    def _register_poc(self):
        poc_string = multiple_replace(self.poc_string, POC_IMPORTDICT)
        path, self.module_name = file_path_parser(self.poc_name)
        try:
            string_importer(self.module_name, poc_string)
        except ImportError as e:
            err_msg = "{0} register failed '{1!s}'".format(self.module_name, e)
            logger.log(CUSTOM_LOGGING.ERROR, err_msg)

    def run(self):
        poc = kb.registered_pocs(self.module_name)

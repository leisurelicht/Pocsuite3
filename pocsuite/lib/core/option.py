#!/usr/bin/env python
# -*- coding: utf-8 -*-
import queue
from oset.pyoset import oset

from pocsuite.lib.core.data import conf
from pocsuite.lib.core.data import kb
from pocsuite.lib.core.datatype import AttribDict
from pocsuite.lib.core.defaults import IS_WIN
from pocsuite.lib.core.defaults import HTTP_DEFAULT_HEADER


def init_options(input_options=None):
    if input_options is None:
        input_options = AttribDict()

    # if IS_WIN:
    #     coloramainit()
    # 好像初始化了没有用

    conf.update(input_options)
    conf.http_headers = HTTP_DEFAULT_HEADER
    conf.params = input_options.extra_params

    if input_options.host:
        conf.http_headers.upadte({'Host': input_options.host})

    try:
        conf.is_poc_string = init_options.is_poc_string
        conf.poc_name = input_options.poc_name
    except Exception:
        conf.is_poc_string = False
        conf.is_pyc_file = False

    initialize_kb()


def initialize_kb():
    kb.targets = queue.Queue()
    kb.pocs = {}
    kb.result = oset()
    kb.registered_pocs = {}

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pocsuite.lib.core.datatype import AttribDict
from pocsuite.lib.core.log import LOGGER
from pocsuite.lib.core.defaults import defaults

# logger
logger = LOGGER

# object to share within function and classes command
# line options and settings
# 应该是主要存储配置信息的
conf = AttribDict()

# Dictionary storing
# (1)targets, (2)registeredPocs, (3) bruteMode
# (4)results, (5)pocFiles
# (6)multiThreadMode \ threadContinue \ threadException
# 貌似这个最重要
kb = AttribDict()

# cmdLineOptionns = AttribDict()

# registeredPocs = {}

# paths = AttribDict()

# defaults = AttribDict(defaults)

# pocJson = AttribDict()

# resultJson = AttribDict()

# saveReq = AttribDict()

# 先全部注释了用到一个解一个

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

from pocsuite.lib.core.enums import CUSTOM_LOGGING

logging.addLevelName(CUSTOM_LOGGING.SYSINFO.value, '*')
logging.addLevelName(CUSTOM_LOGGING.SUCCESS.value, '+')
logging.addLevelName(CUSTOM_LOGGING.ERROR.value, '-')
logging.addLevelName(CUSTOM_LOGGING.WARNING.value, '!')

LOGGER = logging.getLogger('pocsuiteLog')

LOGGER_HANDLER = None

# 下面这一段应该是禁止多彩输出，不过我没有在help中看到相关参数，是被忘了？
disableColor = False

for argument in sys.argv:
    if "disable-col" in argument:
        disableColor = True

        break

if disableColor:
    LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
else:
    try:
        from pocsuite.thirdparty.ansistrm.ansistrm import \
            ColorizingStreamHandler
    except ImportError as e:
        LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
    else:
        LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
        LOGGER_HANDLER.level_map[logging.getLevelName('*')] = (None, "cyan",
                                                               False)
        LOGGER_HANDLER.level_map[logging.getLevelName('+')] = (None, "green",
                                                               False)
        LOGGER_HANDLER.level_map[logging.getLevelName('-')] = (None, "red",
                                                               False)
        LOGGER_HANDLER.level_map[logging.getLevelName('!')] = (None, "yellow",
                                                               False)

FORMATTER = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s",
                              "%H:%M:%S")

LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(CUSTOM_LOGGING.WARNING.value)

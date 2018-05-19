#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
import colorlog

from pocsuite.lib.core.enums import CUSTOM_LOGGING

LOGGER = logging.getLogger('pocsuiteLog')

LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

LOGGER_HANDLER.setFormatter(
    colorlog.ColoredFormatter(
        '%(log_color)s \r[%(asctime)s] [%(levelname).1s] %(message)s',
        "%H:%M:%S"))

LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(CUSTOM_LOGGING.WARNING.value)

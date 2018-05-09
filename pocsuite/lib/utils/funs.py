#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
from pocsuite.lib.core.enums import CUSTOM_LOGGING
from pocsuite.lib.core.data import logger


def str_to_dict(string):
    try:
        return ast.literal_eval(string)
    except ValueError as e:
        logger.log(CUSTOM_LOGGING.ERROR.value,
                   "conv string failed: {}".format(e))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pocsuite.lib.core.data import kb
from pocsuite.lib.core.data import conf
from pocsuite.lib.core.data import paths
from pocsuite.lib.core.data import logger
from pocsuite.lib.core.data import cmd_line_options
from pocsuite.lib.core.common import set_paths

module_path = os.path.dirname(os.path.realpath(__file__))


def pcs_init(pcs_options=None):
    paths.POCSUITE_ROOT_PATH = module_path
    set_paths()


def main():
    """
    main function of pocsuite when running from command line
    """
    pcs_init()

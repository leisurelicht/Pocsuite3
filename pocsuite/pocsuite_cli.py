#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

from pocsuite.lib.core.common import banner, data_to_stdout, set_paths
from pocsuite.lib.core.data import cmd_line_options, conf, kb, logger, paths
from pocsuite.lib.core.defaults import LEGAL_DISCLAIMER
from pocsuite.lib.core.option import init_options
from pocsuite.lib.parse.parser import parse_cmd_options

module_path = os.path.dirname(os.path.realpath(__file__))


def main():
    """
    main function of pocsuite when running from command line
    """
    pcs_init()


def pcs_init(pcs_options=None):
    paths.POCSUITE_ROOT_PATH = module_path
    set_paths()

    if not os.path.exists(paths.POCSUITE_DIR):
        os.makedirs(paths.POCSUITE_OUTPUT_PATH)
    elif not os.path.exists(paths.POCSUITE_OUTPUT_PATH):
        os.mkdir(paths.POCSUITE_OUTPUT_PATH)
    # 应该直接放到set_paths里

    args_dict = pcs_options or parse_cmd_options()
    cmd_line_options.update(args_dict)
    init_options(cmd_line_options)

    if conf.quiet:
        logger.log = None

    banner()
    conf.showTime = True

    data_to_stdout(f"[!] legal disclaimer: {LEGAL_DISCLAIMER}\n\n")
    data_to_stdout(f"[*] starting at {time.strftime('%X')}\n\n")

    if conf.dork:
        pass
        # TODO

    if not any((
            conf.url or conf.url_file,
            conf.requires,
            conf.requires_freeze,
    )):
        err_msg = "No 'url' or 'url_file' or 'dork' assigned."
        sys.exit(logger.error(err_msg))

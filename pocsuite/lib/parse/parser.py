#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from pocsuite.lib.core.defaults import USAGE, VERSION


def parse_cmd_options():
    parser = argparse.ArgumentParser(
        usage=USAGE,
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False,
    )

    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="Show help message and exit",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=VERSION,
        help="Show program's version number and exit",
    )

    target = parser.add_argument_group("target")

    target.add_argument(
        "-u",
        "--url",
        dest="url",
        help="Target URL (e.g. \"http://www.targetsite.com/\")",
    )
    target.add_argument(
        "-f",
        "--file",
        action="store",
        dest="url_file",
        help="Scan multiple targets given in a textual file",
    )
    target.add_argument(
        "-r",
        dest="poc_file",
        help="Load POC from a file (e.g. \"_001_cms_sql_inj.py\") or \
directory (e.g. \"modules/\")",
    )

    mode = parser.add_argument_group("mode")

    mode.add_argument(
        "--verify",
        dest="mode",
        const="verify",
        action="store_const",
        help="Run poc with attack mode",
    )
    mode.add_argument(
        "--attack",
        dest="mode",
        const="attack",
        action="store_const",
        help="Run poc with attack mode",
    )

    request = parser.add_argument_group("request")

    request.add_argument(
        "--cookie",
        dest="cookie",
        help="HTTP Cooike header value",
    )

    request.add_argument(
        "--referer",
        dest="referer",
        help="HTTP Referer header value",
    )

    request.add_argument(
        "--user-agent",
        dest="agent",
        help="HTTP User-Agent header value",
    )

    request.add_argument(
        "--random-agent",
        dest="radom_agent",
        action="store_true",
        default=False,
        help="Use randomly selected HTTP User-Agent header value",
    )

    request.add_argument(
        "--proxy",
        dest="proxy",
        help="Use a proxy to connect to the target URL",
    )

    request.add_argument(
        "--proxy-cred",
        dest="proxy_cred",
        help="Proxy authentication credentials (name:password)",
    )

    request.add_argument(
        "--timeout",
        dest="timeout",
        help="Seconds to wait before timeout connection (default 30s)",
    )

    request.add_argument(
        "--retry",
        dest="retry",
        type=int,
        help="Delay between two request of one thread",
    )

    request.add_argument(
        "--delay",
        dest="delay",
        type=float,
        help="Delay between two request of one thread",
    )

    request.add_argument(
        "--headers",
        dest="headers",
        help="Extra headers (e.g. \"key1: value1\\nkey2: value2\")",
    )

    request.add_argument(
        "--host",
        dest="host",
        help="Host in HTTP headers",
    )

    params = parser.add_argument_group("params")

    params.add_argument(
        "--extra-params",
        dest="extra_params",
        help="Extra params (e.g. \"{username: '****', password: '****'}\")",
    )

    optimization = parser.add_argument_group("optimization")

    optimization.add_argument(
        "--threads",
        dest="threads",
        type=int,
        default=1,
        help="Max number of concurrent HTTP(s) requests (default 1)",
    )

    optimization.add_argument(
        "--report",
        dest="report",
        help="Save a html report to file (e.g. \"./report.html\")",
    )

    optimization.add_argument(
        "--batch",
        dest="batch",
        help="Automatically choose default choice without asking.",
    )

    optimization.add_argument(
        "--quiet",
        dest="quiet",
        action="store_true",
        default=False,
        help="Activate quiet mode, working without logger.",
    )

    optimization.add_argument(
        "--requires",
        dest="requires",
        action="store_true",
        default=False,
        help="Check install_requires",
    )

    optimization.add_argument(
        "--requires-freeze",
        dest="requires_freeze",
        action="store_true",
        default=False,
        help="Check install_requires after register",
    )

    x = parser.add_argument_group("Zoomeye or Seebug")

    x.add_argument(
        "--dork",
        dest="dork",
        action="store",
        default=None,
        help="Zoomeye dork userd for search.",
    )

    x.add_argument(
        "--max-page",
        dest="max_page",
        type=int,
        default=1,
        help="Max page used in Zoomeye API(10 targets/pages)",
    )

    x.add_argument(
        "--search-type",
        dest="search_type",
        action="store",
        default="web, host",
        help="search type used in Zoomeye api, web or host",
    )

    x.add_argument(
        "--vul-keyword",
        dest="vul_keyword",
        action="store",
        default=None,
        help="Seebug keyword used for search",
    )

    args = parser.parse_args()

    return args.__dict__

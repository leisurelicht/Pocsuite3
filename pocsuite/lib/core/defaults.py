#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import sys
import platform

from pocsuite.lib.core.revision import get_revision_number
from pocsuite import __version__

SITE = "http://pocsuite.org"
VERSION = __version__
REVISION = get_revision_number()
FILE_TIME = time.strftime("%Y%m%d", time.gmtime(os.path.getctime(__file__)))

VERSION_STRING = "pocsuite/{0}-{1}".format(VERSION, REVISION or FILE_TIME)

IS_WIN = platform.system() == "Windows"

PLATFORM = os.name

PYVERSION = sys.version.split()[0]

ISSUES_PAGE = "https://github.com/leisurelicht/Pocsuite3/issues"
GIT_REPOSITORY = "git@github.com:leisurelicht/Pocsuite3.git"
GIT_PAGE = "https://github.com/leisurelicht/Pocsuite3"

LEGAL_DISCLAIMER = "Usage of pocsuite for attacking targets without prior \
    mutual consent is illegal."

BANNER = """\033[01;33m
                              ,--. ,--.
 ,---. ,---. ,---.,---.,--.,--`--,-'  '-.,---.  \033[01;37m{\033[01;%dm%s\033[01;37m}\033[01;33m
| .-. | .-. | .--(  .-'|  ||  ,--'-.  .-| .-. :
| '-' ' '-' \ `--.-'  `'  ''  |  | |  | \   --.
|  |-' `---' `---`----' `----'`--' `--'  `----'
`--'                                            \033[0m\033[4;37m%s\033[0m

                  """ % ((31 + hash(REVISION) % 6) if REVISION else 30,
                         VERSION_STRING.split('/')[-1], SITE)

USAGE = "pocsuite [options]"

INDENT = " " * 2

POC_ATTRS = ("vulID", "version", "author", "vulDate", "name", "appVersion",
             "desc", "createDate", "updateDate", "references", "appPowerLink",
             "vulType", "appName")

POC_IMPORTDICT = {
    "from pocsuite.net import":
    "from pocsuite.lib.request.basic import",
    "from pocsuite.poc import":
    "from pocsuite.lib.core.poc import",
    "from pocsuite.utils import register":
    "from pocsuite.lib.core.register import registerPoc as register",
}

POC_REGISTER_STRING = "\nfrom pocsuite.api.poc import register\nregister({})"
POC_REGISTER_REGEX = "register\(.*\)"
POC_CLASSNAME_REGEX = "class\s+(.*?)\(POCBase\)"
POC_REQUIRES_REGEX = "install_requires\s*?=\s*?\[(.*?)\]"

OLD_VERSION_CHARACTER = ("from comm import cmdline",
                         "from comm import generic")

defaults = {
    "threads": 1,
    "timeout": 10,
}

HTTP_DEFAULT_HEADER = {
    "Accept": "*/*",
    "Accept-Charset": "GBK,utf-8;q=0.7,*;q=0.3",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Referer": "http://www.baidu.com",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0"
}

PCS_OPTIONS = {
    'threads': 1,
    'url': None,
    'urlFile': None,
    'agent': None,
    'pocFile': None,
    'isPocString': False,
    'pocname': None,
    'referer': None,
    'Mode': 'verify',
    'cookie': None,
    'randomAgent': False,
    'report': None,
    'proxy': None,
    'proxyCred': None,
    'timeout': 5,
    'quiet': False,
    'requires': False,
    'requiresFreeze': False
}

REPORT_TABLEBASE = """\
    <tbody>
    {0}
    </tbody>
    """

REPORT_HTMLBASE = """\
    <!DOCTYPE html>
    <html lang="zh-cn">
        <head>
            <meta charset="utf-8">
            <title></title>
            <style type="text/css">
            caption{padding-top:8px;padding-bottom:8px;color:#777;text-align:left}th{text-align:left}.table{width:100%%;max-width:100%%;margin-bottom:20px}.table>thead>tr>th,.table>tbody>tr>th,.table>tfoot>tr>th,.table>thead>tr>td,.table>tbody>tr>td,.table>tfoot>tr>td{padding:8px;line-height:1.42857143;vertical-align:top;border-top:1px solid #ddd}.table>thead>tr>th{vertical-align:bottom;border-bottom:2px solid #ddd}.result0{display:none}.result1{}.status{cursor: pointer;}
            </style>
            <script>
                function showDetail(dom){
                    parent = dom.parentElement;
                    detail = parent.children[1];

                    if (detail == undefined){
                        return;
                    };

                    if (detail.className == 'result0'){
                        detail.className = 'result1';
                    }else{
                        detail.className = 'result0';
                    };
                }
            </script>
        </head>
        <body>
            <div class="container">
                <table class="table">
                    <thead>
    {0}
                    </thead>
    {1}
                </table>
            </div>
        </body>
    </html>
    """

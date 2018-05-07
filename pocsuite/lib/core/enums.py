#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class OUTPUT_STATUS(Enum):
    """
    输出信息码
    """
    FAILED = 0
    SUCCESS = 1


class ERROR_TYPE_ID(Enum):
    """
    输出信息错误码
    """
    # PoC 执行时发生 NotImplementedError 异常
    NOTIMPLEMENTEDERROR = 2
    # PoC 执行时发生 ConnectionError 异常
    CONNECTIONERROR = 3.0
    # PoC 执行时发生 HTTPError 异常
    HTTPERROR = 3.1
    # PoC 执行时发生 ConnectTimeout 异常
    CONNECTTIMEOUT = 3.2
    # PoC 执行时发生 HTTPError 异常
    TOMANYREDIRECTS = 3.3
    # PoC 执行时发生其他异常
    OTHER = 4


class CUSTOM_LOGGING(Enum):
    """
    日志信息
    """
    WARNING = 6
    ERROR = 7
    SUCCESS = 8
    SYSINFO = 9


class HTTP_HEADER(Enum):
    ACCEPT = "Accept"
    ACCEPT_CHARSET = "Accept-Charset"
    ACCEPT_ENCODING = "Accept-Encoding"
    ACCEPT_LANGUAGE = "Accept-Language"
    AUTHORIZATION = "Authorization"
    CACHE_CONTROL = "Cache-Control"
    CONNECTION = "Connection"
    CONTENT_ENCODING = "Content-Encoding"
    CONTENT_LENGTH = "Content-Length"
    CONTENT_RANGE = "Content-Range"
    CONTENT_TYPE = "Content-Type"
    COOKIE = "Cookie"
    SET_COOKIE = "Set-Cookie"
    HOST = "Host"
    LOCATION = "Location"
    PRAGMA = "Pragma"
    PROXY_AUTHORIZATION = "Proxy-Authorization"
    PROXY_CONNECTION = "Proxy-Connection"
    RANGE = "Range"
    REFERER = "Referer"
    SERVER = "Server"
    USER_AGENT = "User-Agent"
    TRANSFER_ENCODING = "Transfer-Encoding"
    URI = "URI"
    VIA = "Via"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import exceptions as reqex

from pocsuite.lib.core.data import conf
from pocsuite.lib.core.data import logger
from pocsuite.lib.core.enums import ERROR_TYPE_ID
from pocsuite.lib.core.enums import CUSTOM_LOGGING
from pocsuite.lib.core.enums import OUTPUT_STATUS
from pocsuite.lib.core.common import parse_target_url
from pocsuite.api.utils import str_to_dict


class POCBase:
    """
    所有POC类的基础
    """

    def _verify(self):
        """
        以Poc的verify模式对urls进行检测(可能具有危险性)
        需要在用户自定义的Poc中进行重写
        返回一个Output类实例
        """
        raise NotImplementedError

    def _attack(self):
        """
        以Poc的verify模式对urls进行检测(可能具有危险性)
        需要在用户自定义的Poc中进行重写
        返回一个Output类实例
        """
        raise NotImplementedError

    def execute(self,
                target,
                headers=None,
                params=None,
                mode='verify',
                verbose=True):
        """
        url: the target url
        headers: a class dict include some fields for request header
        params: a instance of Params, include extra params
        """
        self.target = target
        self.url = parse_target_url(target)
        self.header = headers
        self.params = params and str_to_dict(params) or {}
        self.mode = mode
        self.verbose = verbose
        self.exception = None

        try:
            call = [self._attack, self.verify][self.mode == 'verify']
            output = call()
        except NotImplementedError as e:
            self.exception = (ERROR_TYPE_ID.NOTIMPLEMENTEDERROR.value, e)
            logger.log(CUSTOM_LOGGING.ERROR,
                       "POC: '{}' not defined '{}' mode.".format(
                           self.name, self.mode))
            output = Output(self)
        except reqex.ConnectTimeout as e:
            self.exception = (ERROR_TYPE_ID.CONNECTTIMEOUT.value, e)

            while conf.retry > 0:
                logger.log(CUSTOM_LOGGING.WARNING.value,
                           "POC: '{}' timeout, start it over.".foramt(
                               self.name))
                try:
                    output = call()
                except reqex.ConnectTimeout:
                    logger.log(CUSTOM_LOGGING.WARNING.value,
                               "POC: '{}' timeout, start it over.".foramt(
                                   self.name))
                conf.retry -= 1
            else:
                logger.log(CUSTOM_LOGGING.ERROR.value, str(e))
            output = Output(self)

        except reqex.HTTPError as e:
            self.exception = (ERROR_TYPE_ID.HTTPERROR.value, e)
            logger.log(CUSTOM_LOGGING.WARNING,
                       "POC: '{}' HTTPError occurs, start it over.".format(
                           self.name))
            output = Output(self)

        except reqex.ConnectionError as e:
            self.exception = (ERROR_TYPE_ID.CONNECTIONERROR.value, e)
            logger.log(CUSTOM_LOGGING.ERROR, str(e))
            output = Output(self)

        except reqex.TooManyRedirects as e:
            self.exception = (ERROR_TYPE_ID.TOOMANYREDIRECTS.value, e)
            logger.log(CUSTOM_LOGGING.ERROR, str(e))
            output = Output(self)

        except Exception as e:
            self.exception = (ERROR_TYPE_ID.OTHER.value, e)
            logger.log(CUSTOM_LOGGING.ERROR.value, str(e))
            output = Output(self)

        return output


class Output:
    def __init__(self, poc=None):
        self.error = ''

        if poc is not None:
            self.url = poc.url
            self.mode = poc.mode
            self.vul_id = poc.vulID
            self.name = poc.name
            self.app_name = poc.appName
            self.app_version = poc.appVersion
            self.error = poc.exception
        self.result = {}
        self.status = OUTPUT_STATUS.FAILED.value

    def is_success(self):
        return bool(self.status)

    def success(self, result):
        assert isinstance(result, dict)
        self.status = OUTPUT_STATUS.SUCCESS.value
        self.result = result

    def fail(self, error):
        self.status = OUTPUT_STATUS.FAILED.value
        assert isinstance(error, str)

        if isinstance(self.error, str):
            error = (0, error)
        self.error = error

    def show_ersult(self):
        if self.status == OUTPUT_STATUS.SUCCESS.value:
            info_msg = "poc-{0} '{1}' has already been detected against '{2}'.".format(
                self.vul_id, self.name, self.url)
            logger.log(CUSTOM_LOGGING.SUCCESS, info_msg)

            for k, v in self.result.items():
                if isinstance(v, dict):
                    for kk, vv in v.items():
                        logger.log(CUSTOM_LOGGING.SUCCESS.value,
                                   "{} : {}".foramt(kk, vv))
                else:
                    logger.log(CUSTOM_LOGGING.SUCCESS, "{} : {}".format(k, v))
        else:
            err_msg = "poc-{} '{}' failed.".format(self.vul_id, self.name)
            logger.log(CUSTOM_LOGGING.ERROR.value, err_msg)

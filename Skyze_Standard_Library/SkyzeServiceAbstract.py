"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json
import logging
import rollbar

# Skyze Imports
import settings_skyze
from Skyze_Standard_Library.ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
from Skyze_Standard_Library.SkyzeLogger import *
# Skyze Messages
from Skyze_Messaging_Service.Messages.SkyzeMessageTypes import *
from Skyze_Messaging_Service.Messages.MessageSchedulerRun import MessageSchedulerRun


class SkyzeServiceAbstract(object):
    """Skyze Base class for services"""

    def __init__(self, message_bus=None, log_path="", print_log=True):
        """Constructor"""
        self._created = datetime.now()
        self._message_bus = message_bus
        self._print_log = print_log

        # Create Logger
        logger_class_name = self.getType()
        self._logger = SkyzeLogger(logger_class_name, log_path)
        log_message = f"{self.getType()}::__init__::Started"
        self._logger.log_info(log_message, False)

    def getType(self):
        return self.__class__.__name__

    def getPrintLog(self):
        return self._print_log

    def setPrintLog(self, print_log):
        self._print_log = print_log

    def _sendMessage(self, message):
        log_msg = f"{self.getType()}::Send Msg::{message.getJSON()}"
        self._logger.log_info(log_msg)
        self._message_bus.publishMessage(message)

    def _unknownMessageTypeError(self, message):
        log_msg = f"{self.__class__.__name__}::Unknown Message Type Error"
        log_msg += f"\ntype: {type(message)}\n{message.getJSON()}"
        self._logger.log_info(log_msg)
        raise IOError

    def receiveMessage(self, message):
        log_msg = f"{self.getType()}::receiveMessage::{message.getJSON()}"
        self._logger.log_info(log_msg)

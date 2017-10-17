"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json
import logging

# Skyze Imports
import ExceptionSkyzeAbstract
from Skyze_Standard_Library.SkyzeLogger import *
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
        log_message = f"Log: {self.getType()} Started"
        self._logger.log_info(log_message, self._print_log)

    def getType(self):
        return self.__class__.__name__

    def getPrintLog(self):
        return self._print_log

    def setPrintLog(self, print_log):
        self._print_log = print_log

    def _sendMessage(self, message):
        self._message_bus.publishMessage(message)

    def _unknownMessageTypeError(self, message):
        print(f"{self.__class__.__name__} Unknown Message Type {message.getJSON()}")
        print("message ... Message type: " + str(message_type))
        print(" type: " + str(type(message_type)))
        raise IOError

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

    def __init__(self, message_bus=None, log_path=""):
        """Constructor"""
        self._created = datetime.now()
        self._message_bus = message_bus

        # Create Logger
        logger_class_name = self.getType()
        self._log = SkyzeLogger(logger_class_name, log_path)
        print(f"Log: {self.getType()} Started")
        self._log.log_info(f"Log: {self.getType()} Started")

    def mike__init__(self, message_bus=None, log_path=""):
        """Constructor"""
        self._created = datetime.now()
        self._message_bus = message_bus

        # Logging
        # TODO: move logging code to standard library
        if log_path != "":
            log_path = log_path + "/"
        logger_name = f"{self.getType()}_logger"
        log_file = f'{log_path}Logs/Skyze_Log_{self.getType()}.log'
        level = logging.INFO
        #self.__setup_logger(logger_name, log_file_name)
        # TODO convert this to a function as below
        # It didn't work below as it kept mistaking the logger_name string
        # as a message bus object !!!
        l = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(asctime)s : %(message)s')
        fileHandler = logging.FileHandler(log_file, mode='a')
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        l.setLevel(level)
        l.addHandler(fileHandler)
        l.addHandler(streamHandler)
        # End of Function

        # Do some Loggings
        log = logging.getLogger(logger_name)
        # log!
        print(f"Log: {self.getType()} Started")
        log.info(f"Log: {self.getType()} Started")

    def __setup_logger(logger_name, log_file, level=logging.INFO):
        """From https://stackoverflow.com/questions/17035077/python-logging-to-multiple-log-files-from-different-classes"""
        print("Here")
        print(logger_name)
        print(type(logger_name))
        l = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(asctime)s : %(message)s')
        fileHandler = logging.FileHandler(log_file, mode='a')
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        l.setLevel(level)
        l.addHandler(fileHandler)
        l.addHandler(streamHandler)

    def getType(self):
        return self.__class__.__name__

    def _sendMessage(self, message):
        self._message_bus.publishMessage(message)

    def _unknownMessageTypeError(self, message):
        print(f"{self.__class__.__name__} Unknown Message Type {message.getJSON()}")
        print("message ... Message type: " + str(message_type))
        print(" type: " + str(type(message_type)))
        raise IOError

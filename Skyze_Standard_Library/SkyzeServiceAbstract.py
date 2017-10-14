"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json

# Skyze Imports
import ExceptionSkyzeAbstract
from Skyze_Messaging_Service.Messages.SkyzeMessageTypes import *


class SkyzeServiceAbstract(object):
    """Skyze Base class for services"""

    def __init__(self, message_bus=None):
        """Constructor"""
        self._created = datetime.now()
        self._message_bus = message_bus
        print(f"Log: {self.getType()} Started")

    def getType(self):
        return self.__class__.__name__

    def _sendMessage(self, message):
        self._message_bus.publishMessage(message)

    def _unknownMessageTypeError(self, message):
        print(f"{self.__class__.__name__} Unknown Message Type {message.getJSON()}")
        print("message ... Message type: " + str(message_type))
        print(" type: " + str(type(message_type)))
        raise IOError

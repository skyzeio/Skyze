"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json

# Skyze Imports
from Skyze_Standard_Library.ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
from Skyze_Messaging_Service.Messages.SkyzeMessageTypes import *


class MessageSkyzeAbstract(object):
    """Skyze inter-service messages"""

    def __init__(self, message_type):
        """Constructor"""
        self.__created = str(datetime.now())
        self.__message_type = message_type

    def getCreated(self):
        """Getter"""
        return self.__created

    def getMessageType(self):
        """Getter"""
        return self.__message_type

    def getJSON(self):
        """Getter example
        {"_MessageSkyzeAbstract__created":     "2017-10-12 12:54:07.603127",
         "_MessageSkyzeAbstract__type":        "MessageType.NULL",
         "_MessageDataReceived__exchange":     "Cryptopia",
         "_MessageDataReceived__market_pair":  "BTC_USDT",
         "_MessageDataReceived__interval":     "5_min",
         "_MessageDataReceived__message_content": "Cryptopia:BTC_USDT:5_min"}"""
        return f'{{"created": "{self.__created}", "type": "{self.__message_type}"'

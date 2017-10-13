"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json

# Skyze Imports
from Skyze_Standard_Library.SkyzeServiceAbstract import *


class SkyzeMessageBusService(SkyzeServiceAbstract):
    """Skyze inter-service message bus"""

    def __init__(self):
        """Constructor"""
        super().__init__()

    def setServices(self, market_data_updater, message_logger, scheduler, screener):
        """Sets the services pub/sub to the bus"""
        self.__market_data_updater = market_data_updater
        self.__market_message_logger = message_logger
        self.__scheduler = scheduler
        self.__screener = screener

    def getCreated(self):
        """Getter"""
        return self.__created

    def getJSON(self):
        """Getter"""
        return json.dumps(self.__dict__)

    def publishMessage(self, published_message):
        """Publishes Messages"""
        self.__route_message(published_message)

    def __route_message(self, message):
        """Sends message to apprpriate receiver"""
        if message.getType() == SkyzeMessageType.NEW_MARKET_DATA:
            self.__screener.receiveNewMarketData(message)
        else:
            # raise exception - Message not identified
            pass

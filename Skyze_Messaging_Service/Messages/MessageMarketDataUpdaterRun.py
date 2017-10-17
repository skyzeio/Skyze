"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageMarketDataUpdaterRun(MessageSkyzeAbstract):
    """Data has been fully loaded and ready for use"""

    def __init__(self, exchange, interval, market_pairs=None):
        """Constructor"""
        super().__init__(SkyzeMessageType.MARKET_DATA_UPDATER_RUN)
        self.__exchange = exchange
        self.__market_pairs = market_pairs
        self.__interval = interval
        self.__message_content = f"{exchange}:{market_pairs}:{interval}"

    def getMarketPair(self):
        """Getter"""
        return self.__market_pairs

    def getExchange(self):
        """Getter"""
        return self.__exchange

    def getInterval(self):
        """Getter"""
        return self.__interval

    def getMessageContent(self):
        """Getter"""
        return self.__message_content

    def getJSON(self):
        """Return object as JSON"""
        return super().getJSON()  # json.dumps(self.__dict__)

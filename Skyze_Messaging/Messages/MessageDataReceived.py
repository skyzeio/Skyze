"""Created on 08/09/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging.Messages.MessageSkyzeAbstract import *


class MessageDataReceived(MessageSkyzeAbstract):
    """Data has been fully loaded and ready for use"""

    __message_type = "Data Received"

    def __init__(self, exchange, market_pair, interval):
        """Constructor"""
        super().__init__()
        self.__exchange = exchange
        self.__market_pair = market_pair
        self.__interval = interval
        self.__message_content = f"{exchange}:{market_pair}:{interval}"

    def getMessageType(self):
        """Getter"""
        return self.__message_type

    def getMarketPair(self):
        """Getter"""
        return self.__market_pair

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
        return json.dumps(self.__dict__)

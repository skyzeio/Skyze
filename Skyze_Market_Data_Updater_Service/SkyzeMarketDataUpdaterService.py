"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json

# Skyze Imports
from Skyze_Standard_Library.SkyzeServiceAbstract import *


class SkyzeMarketDataUpdaterService(SkyzeServiceAbstract):
    """Skyze inter-service message logger"""

    def __init__(self, message_bus):
        """Constructor"""
        super().__init__(message_bus)

    def run_update(self, exchange, market_pair, interval):
        print(
            f"Mkt Data Updater Serivce: run_update {exchange},{market_pair},{interval}")

    def run_update_all(self):
        print(f"Mkt Data Updater Serivce: run_update all")

    def receiveMessage(self, message_received):
        """Gets the mssage from the bus and routes internally"""
        # Route to appropriate service
        message_type = message_received.getMessageType()
        if message_type == SkyzeMessageType.MARKET_DATA_UPDATER_RUN:
            self.run_update(message_received.getExchange(),
                            message_received.getMarketPair(),
                            message_received.getInterval())
        elif message_type == SkyzeMessageType.MARKET_DATA_UPDATER_RUN_ALL:
            self.run_update_all()
        else:
            self._unknownMessageTypeError(message_received)

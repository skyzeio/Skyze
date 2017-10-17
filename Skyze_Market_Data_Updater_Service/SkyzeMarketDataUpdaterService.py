"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json

# Skyze Imports
# Settings
import settings_skyze
from Skyze_Market_Data_Updater_Service import settings
# Exchanges and other data sources
from Skyze_Market_Data_Updater_Service.CoinMarketCap import CoinMarketCap
from Skyze_Market_Data_Updater_Service.Cryptopia import Cryptopia
from Skyze_Market_Data_Updater_Service.PoloniexSkyze import PoloniexSkyze
# Parent class
from Skyze_Standard_Library.SkyzeServiceAbstract import *


class SkyzeMarketDataUpdaterService(SkyzeServiceAbstract):
    """Skyze inter-service message logger"""

    def __init__(self, message_bus):
        """Constructor"""
        self._path_to_service = "Skyze_Market_Data_Updater_Service"
        super().__init__(message_bus=message_bus, log_path=self._path_to_service)

    def __get_class(self, kls):
        """ Helper function to create a class from a string
            From: https://stackoverflow.com/questions/452969/does-python-have-an-equivalent-to-java-class-forname"""
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m

    def run_update(self, exchange_name, market_pairs, interval):
        # log
        log_message = f"Mkt Data Updater Serivce: run_update \
                            {exchange_name},{market_pairs},{interval}"
        self._logger.log_info(log_message, self._print_log)

        # Create the exchange object and run the update
        if exchange_name == "Cryptopia":
            exchange = Cryptopia(self._message_bus, self._logger)
        elif exchange_name == "CoinMarketCap":
            exchange = CoinMarketCap(self._message_bus, self._logger)
        elif exchange_name == "Poloniex":
            exchange = PoloniexSkyze(self._message_bus, self._logger)
        elif exchange == "TODO Dynamic Creation":
            # TODO construct the exchange class from the classs name string
            #      won't have to do the above if/elif ....
            # from https://stackoverflow.com/questions/452969/does-python-have-an-equivalent-to-java-class-forname
            class_name = settings_skyze.exchanges.get_value(
                exchange_name, "Class_name")
            exchange_class_name = f'{self._path_to_service}.{ex_cls_name}'
            # exchange_class_name = settings_skyze.exchanges.get_value(
            #    exchange_name, "Class_name")
            print(exchange_name)
            print(exchange_class_name)
            #m = __import__("Skyze_Market_Data_Updater_Service.Cryptopia")
            #m1 = getattr(m, "Cryptopia")
            #exchange = getattr(m1, "Cryptopia")
            exchange = self.__get_class(exchange_class_name)
            print(type(exchange))
        else:
            # Unknown exchange sent
            rollbar.report_exc_info()
            raise IOError

        # Run the update
        if market_pairs == None:
            exchange.updateMarketData()
        else:
            exchange.updateMarketData(market_pairs)

    def run_update_all(self):
        self._logger.log_info(
            "Mkt Data Updater Serivce: run_update all", self._print_log)

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

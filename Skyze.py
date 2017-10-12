"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party libraries

# Skyze libraries
from Skyze_Market_Data_Updater_Service.SkyzeMarketDataUpdaterService import *
from Skyze_Message_Logger_Service.SkyzeMessageLoggerService import *
from Skyze_Messaging_Service.SkyzeMessagingBusService import *
from Skyze_Scheduler_Service.SkyzeSchedulerService import *
from Skyze_Screener_Service.SkyzeScreenerService import *


class Skyze(object):
    """Starts up all the Skyzes Services"""

    def __init__(
        self,
        market_data_update_service=None,
        message_logger=None,
        messaging_service=None,
        scheduler_service=None,
        screener_service=None
    ):
        """Constructor - allocates private variables"""
        self.__messaging_service = messaging_service
        self.__market_data_update_service = market_data_update_service
        self.__scheduler_service = scheduler_service
        self.__screener_service = screener_service
        self.__message_logger = message_logger

    def __start_up_skyze(self):
        """Starts all the Skyze Services and ensures the Message Serivce
           knows where all the other services are and that each Serivce
           knows where the messageing serice is"""
        if self.__messaging_service is None:
            self.__messaging_service = SkyzeMessageBus()

        if self.__message_logger is None:
            self.__message_logger = SkyzeMessageLogger(
                self.__messaging_service)

        if self.__market_data_updater is None:
            self.__market_data_updater = SkyzeMarketDataUpdater(
                self.__messaging_service)

        if self.__screener is None:
            self.__screener = SkyzeScreener(self.__messaging_service)

        if self.__scheduler is None:
            self.__scheduler = SkyzeScheduler(self.__messaging_service)

        self.__messaging_service.setServices(self.__message_logger,
                                             self.__market_data_updater,
                                             self.__screener,
                                             self.__scheduler
                                             )

    def run(self):
        """Starts all Skyzes Servcies"""
        self.__start_up_skyze()

"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party libraries
from halo import Halo

# Skyze libraries
import settings_skyze
from Skyze_Market_Data_Cleaner_Service.SkyzeMarketDataCleanerService import *
from Skyze_Market_Data_Updater_Service.SkyzeMarketDataUpdaterService import *
from Skyze_Message_Logger_Service.SkyzeMessageLoggerService import *
from Skyze_Notifier_Service.SkyzeNotifierService import *
from Skyze_Messaging_Service.SkyzeMessageBusService import *
from Skyze_Scheduler_Service.SkyzeSchedulerService import *
from Skyze_Screener_Service.SkyzeScreenerService import *


class Skyze(object):
    """Starts up all the Skyzes Services"""

    def __init__(
        self,
        market_data_cleaner_service=None,
        market_data_update_service=None,
        message_logger=None,
        messaging_service=None,
        notifier_service=None,
        scheduler_service=None,
        screener_service=None
    ):
        """Constructor - allocates private variables"""
        self.__market_data_cleaner_service = market_data_cleaner_service
        self.__market_data_update_service = market_data_update_service
        self.__messaging_service = messaging_service
        self.__notifier_service = notifier_service
        self.__scheduler_service = scheduler_service
        self.__screener_service = screener_service
        self.__message_logger_service = message_logger
        print("\n\n=== SkyZe Starting +++++++++")

        # Rollbar Error reporting
        run_env = f"{settings_skyze.run_environment} - {self.getType()}"
        rollbar_on = False
        if rollbar_on:
            rollbar.init(settings_skyze.rollbar_access_token, run_env)
            rollbar.report_message(
                f"{run_env} - Rollbar is configured correctly")

    def getType(self):
        return self.__class__.__name__

    def __start_up_skyze_services(self):
        """Starts all the Skyze Services and ensures the Message Serivce
           knows where all the other services are and that each Serivce
           knows where the messageing serice is"""

        # Note thatthe order of serivce creation is important
        if self.__messaging_service is None:
            self.__messaging_service = SkyzeMessageBusService()

        if self.__message_logger_service is None:
            self.__message_logger_service = SkyzeMessageLoggerService(
                self.__messaging_service)

        if self.__notifier_service is None:
            self.__notifier_service = SkyzeNotifierService(
                self.__messaging_service)

        if self.__market_data_update_service is None:
            self.__market_data_update_service = SkyzeMarketDataUpdaterService(
                self.__messaging_service)

        if self.__scheduler_service is None:
            self.__scheduler_service = SkyzeSchedulerService(
                self.__messaging_service)

        if self.__screener_service is None:
            self.__screener_service = SkyzeScreenerService(
                self.__messaging_service)

        if self.__market_data_cleaner_service is None:
            self.__market_data_cleaner_service = SkyzeMarketDataCleanerService(
                self.__messaging_service)

        self.__messaging_service.setServices(self.__market_data_cleaner_service,
                                             self.__market_data_update_service,
                                             self.__message_logger_service,
                                             self.__notifier_service,
                                             self.__scheduler_service,
                                             self.__screener_service
                                             )

        print("=== SkyZe All services started +++++++++")

    def __send_market_message(self):
        market_list = ['ETH_BTC', 'LTC_BTC', 'HSR_BTC',
                       'PAC_DOGE', 'SPR_BTC', 'ODN_BTC']

        msg = MessageMarketDataUpdaterRun("Cryptopia", market_list, "Tick")
        print(
            f"Sending Cryptopia Update message - {datetime.now()} - {msg.getJSON()}")
        self.__messaging_service.publishMessage(msg)

    def run(self):
        """Starts all Skyzes Servcies then processes messages"""
        # Start services
        self.__start_up_skyze_services()

        # Test batches of messages
        if False:
            self.__send_market_message()
        if False:
            msg = MessageSchedulerTest()
            self.__messaging_service.publishMessage(msg)

        # Start Skyze by messaging the scheduler to invoke it's schedule
        msg = MessageSchedulerRun()
        self.__messaging_service.publishMessage(msg)

        # Process messages - invokes the messaging service to infinitely
        # loop looking for messages to route
        spinner = Halo(
            text='SkyZe is alive ... Processing Messages', spinner='dots')
        # spinner.start()
        print("\n\n")
        self.__messaging_service.process_messages()
        # spinner.stop()

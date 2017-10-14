# 3rd Party Libraries
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from random import randint

# Skyze Imports
from Skyze_Standard_Library.SkyzeServiceAbstract import *
from Skyze_Messaging_Service.Messages.MessageMarketDataUpdaterRun import MessageMarketDataUpdaterRun
from Skyze_Messaging_Service.Messages.MessageMarketDataUpdaterRunAll import MessageMarketDataUpdaterRunAll
from Skyze_Messaging_Service.Messages.MessageScreenerRun import MessageScreenerRun


class SkyzeSchedulerService(SkyzeServiceAbstract):
    """Skyze inter-service message logger"""

    def __init__(self, message_bus):
        """Constructor"""
        #self.__message_bus = None
        super().__init__(message_bus)

    def __sendMessage(self, message):
        self._message_bus.publishMessage(message)

    def test(self):
        start_time = datetime.now()
        print('=== Skyze Scheduler TEST RUN ========== ' +
              str(start_time) + ' ========== ')
        print()

        sched = BlockingScheduler()

        message_list = [
            MessageMarketDataUpdaterRun("Poloniex", "BTCUSD", "1_Hour"),
            MessageMarketDataUpdaterRunAll("Cryptopia"),
            MessageScreenerRun("Mike's Screener")
        ]

        for i in range(1, 10):
            msg_number = randint(0, 2)
            msg = message_list[msg_number]
            self._sendMessage(msg)
        print("Test Messages published")

    def start(self):
        start_time = datetime.now()
        print('=== Skyze Scheduler ========== ' +
              str(start_time) + ' ========== ')
        print()

        sched = BlockingScheduler()

        @sched.scheduled_job('cron', day_of_week='mon-sun', hour='0-23')
        def cryptopia_hourly_update():
            message = 'Scheduler:: Triggering:: cryptopia_hourly_update'
            print(message)
            send_message(message)

        """Fold this back into start function when ready"""
        @sched.scheduled_job('cron', day_of_week='mon-sun', hour=14, minute=30)
        def cmc_daily_update():
            message = 'Scheduler:: Triggering:: CMC all markets Daily Update at 2:30pm.'
            print(message)
            send_message(message)

        @sched.scheduled_job('cron', day_of_week='mon-sun', hour=10, minute=12)
        def poloniex_daily_update():
            message = 'Scheduler:: Triggering:: Poloniex all markets Daily Update at 10:12am'
            print(message)
            send_message(message)

        sched.print_jobs()
        print("SCHEDULER NOT STARTED\n\n")
        # sched.start()

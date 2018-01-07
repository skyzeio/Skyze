# 3rd Party Libraries
#from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from random import randint

# Skyze Imports
from Skyze_Scheduler_Service import settings
from Skyze_Standard_Library.SkyzeServiceAbstract import *
# Messages
from Skyze_Messaging_Service.Messages.MessageMarketDataUpdaterRun \
    import MessageMarketDataUpdaterRun
from Skyze_Messaging_Service.Messages.MessageMarketDataUpdaterRunAll \
    import MessageMarketDataUpdaterRunAll
from Skyze_Messaging_Service.Messages.MessageScreenerRun import MessageScreenerRun
from Skyze_Messaging_Service.Messages.MessageSchedulerRun import MessageSchedulerRun
from Skyze_Messaging_Service.Messages.MessageSchedulerTest import MessageSchedulerTest


class SkyzeSchedulerService(SkyzeServiceAbstract):
  """Skyze inter-service message logger"""

  def __init__(self, message_bus):
    """Constructor
       Scheduler doco: http://apscheduler.readthedocs.io/en/latest/userguide.html"""
    #self.__message_bus = None
    path_to_service = "Skyze_Scheduler_Service"
    super().__init__(message_bus=message_bus, log_path=path_to_service)

    # Create Scheduler
    # BlockingScheduler: use when the scheduler is the only thing
    #                    running in your process
    # BackgroundScheduler: use when you’re not using any of the
    #             frameworks below, and want the scheduler to run
    #             in the background inside your application
    self._sched = BackgroundScheduler()

  def test(self):
    start_time = datetime.now()
    print('=== Skyze Scheduler TEST RUN ========== ' +
          str(start_time) + ' ========== ')
    print()

    market_list = ['ETH_BTC', 'LTC_BTC', 'HSR_BTC',
                   'PAC_DOGE', 'SPR_BTC', 'ODN_BTC']
    message_list = [
        MessageMarketDataUpdaterRun("Cryptopia", market_list, "Tick"),
        MessageMarketDataUpdaterRunAll("Poloniex"),
        MessageScreenerRun("Mike's Screener")
    ]

    for i in range(1, 10):
      msg_number = randint(0, 2)
      msg = message_list[msg_number]
      self._sendMessage(msg)
    print(f"Test Messages published")

  def send_random_message(self):
    market_list = ['ETH_BTC', 'LTC_BTC', 'HSR_BTC',
                   'PAC_DOGE', 'SPR_BTC', 'ODN_BTC']

    message_list = [
        MessageMarketDataUpdaterRun("Cryptopia", market_list, "Tick"),
        MessageMarketDataUpdaterRunAll("Poloniex"),
        MessageScreenerRun("Mike's Screener")
    ]

    msg_number = randint(0, 2)
    msg = message_list[msg_number]
    log_msg = f"Scheduler Service::send_random_message - {datetime.now()} - {msg.getJSON()}"
    self._logger.log_info(log_msg)
    self._sendMessage(msg)

  # ========================================================================
  # ----- Jobs to Schedule =================================================
  # ========================================================================
  def bitfinex_90min_update(self, market_pairs=None):
    log_msg = 'Scheduler:: Triggering:: Bitfinex 90 minute Update'
    self._logger.log_info(log_msg)
    pairs = []
    message = MessageMarketDataUpdaterRun(
        "Bitfinex", "All", market_pairs=pairs)
    self._sendMessage(message)

  #@sched.scheduled_job('cron', day_of_week='mon-sun', hour='0-23', minute=1)
  def cryptopia_hourly_update(self, market_pairs=None):
    log_msg = 'Scheduler:: Triggering:: Cryptopia Hourly Update'
    self._logger.log_info(log_msg)
    hourly_pairs = ['ETH_BTC', 'LTC_BTC',
                    'HSR_BTC', 'PAC_DOGE', 'SPR_BTC', 'ODN_BTC']
    message = MessageMarketDataUpdaterRun(
        "Cryptopia", "Tick", market_pairs=hourly_pairs)
    self._sendMessage(message)

  def cryptopia_daily_update(self, market_pairs=None):
    log_msg = 'Scheduler:: Triggering:: Cryptopia Hourly Update'
    self._logger.log_info(log_msg)
    message = MessageMarketDataUpdaterRun(
        "Cryptopia", "Tick", market_pairs=None)
    self._sendMessage(message)

  #@sched.scheduled_job('cron', day_of_week='mon-sun', hour=14, minute=30)
  def cmc_daily_update(self, market_pairs=None):
    log_msg = 'Scheduler:: Triggering: : CMC all markets Daily Update at 2: 30pm.'
    self._logger.log_info(log_msg)
    message = MessageMarketDataUpdaterRun(
        "CoinMarketCap", "Daily", market_pairs=None)
    self._sendMessage(message)

  #@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10, minute=12)
  def poloniex_daily_update(self, market_pairs=None):
    log_msg = 'Scheduler:: Triggering:: Poloniex all markets Daily Update at 10:12am'
    self._logger.log_info(log_msg)
    message = MessageMarketDataUpdaterRun(
        "Poloniex", "All", market_pairs=None)
    self._sendMessage(message)

  # ========================================================================
  # ====== Start the Scheduler =============================================
  # ========================================================================
  def start(self):
    """Schedules the jobs and starts the scheduler"""
    start_time = datetime.now()
    print('=== Skyze Scheduler ========== ' +
          str(start_time) + ' ==========\n')

    # === Create the scheduled jobs
    # TODO Get list of jobs from settings file
    #job = sched.add_job(self.send_random_message, 'interval', minutes=1)

    # Bitfinex 90 minute-ly for all markets
    job = self._sched.add_job(self.bitfinex_90min_update,
                              'interval', minutes=90)

    # Cryptopia Daily - hourly for high volume markets
    job = self._sched.add_job(self.cryptopia_hourly_update,
                              'cron', day_of_week='mon-sun', hour='0-23')
    #                          'interval', hours=1)

    # Poloniex only needs daily update - as can request that much history
    job = self._sched.add_job(self.poloniex_daily_update, 'cron',
                              day_of_week='mon-sun', hour=20, minute=12)  # 20:12
    # Cryptopia Daily run 1 - twice a day for low volume markets
    job = self._sched.add_job(self.cryptopia_daily_update, 'cron',
                              day_of_week='mon-sun', hour=21, minute=35)  # 21:35
    # CoinMarketCap Daily update - as can request that much history
    job = self._sched.add_job(self.cmc_daily_update, 'cron',
                              day_of_week='mon-sun', hour=1, minute=8)  # 01:08
    # Cryptopia Daily run 2 - twice a day for low volume markets
    job = self._sched.add_job(self.cryptopia_daily_update, 'cron',
                              day_of_week='mon-sun', hour=8, minute=8)  # 08:08

    # === Print the list of jobs and start the scheduler
    self._sched.print_jobs()
    self._sched.start()

  def receiveMessage(self, message_received):
    """Gets the messages from the bus, unpacks any data and routes internally"""
    # Parent class processing
    super().receiveMessage(message_received)
    # Route to appropriate service
    message_type = message_received.getMessageType()
    if message_type == SkyzeMessageType.SCHEDULER_RUN:
      self.start()
    elif message_type == SkyzeMessageType.SCHEDULER_TEST:
      self.test()
    else:
      self._unknownMessageTypeError(message_received)

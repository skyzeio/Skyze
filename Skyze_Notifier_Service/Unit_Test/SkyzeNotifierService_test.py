"""Created on 9 / 1 / 2018 @author: michaelnew"""


# Standard Libraries
import ccxt

# Skyze libraries - Required
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *
import Skyze_Standard_Library.Colourful_Printing as cp

# Skyze libraries - Test Case Specific
from Skyze_Notifier_Service.SkyzeNotifierService import *
from Skyze_Messaging_Service.SkyzeMessageBusService import *
from Skyze_Messaging_Service.Messages.MessageMarketDataUpdaterRunComplete \
    import MessageMarketDataUpdaterRunComplete


class SkyzeNotifierService_test(UnitTestSkyzeAbstract):
  """Test the SkyzeNotifierService Class"""

  _package_name = "Skyze_Notifer_Service"
  _class_tested = "SkyzeNotifierService"

  #@unittest.skip("Working on new test")
  def test__sendTweet(self):
    # Set up for testing
    # logger_class_name = self.__class__.__name__
    # logger = SkyzeLogger(logger_class_name, "")
    # log_message = f"{logger_class_name}::__init__::Started"
    package_name = "Skyze Notifier Service"
    test_name = "__sendTweet"
    test_file = target_file = test_columns = "N/A"
    self.printTestHeader(package_name, test_name, test_file,
                         target_file, test_columns)

    message_bus = SkyzeMessageBusService()
    notifier_service = SkyzeNotifierService(message_bus)

    source_name = "Bitfinex"
    exchange_intervals = []
    error_list = []

    print("\n\tsource_name: " + source_name +
          "\texchange_intervals: " + str(exchange_intervals) +
          "\terror_list: " + str(error_list))

    end_run_msg = MessageMarketDataUpdaterRunComplete(
        source_name, exchange_intervals, len(error_list),
        error_list, market_pairs=None)
    notifier_service.receiveMessage(end_run_msg)


if __name__ == '__main__':
  unittest.main()

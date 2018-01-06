"""Created on 3 / 1 / 2018 @author: michaelnew"""


# Standard Libraries
import ccxt

# Skyze libraries - Required
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *
import Skyze_Standard_Library.Colourful_Printing as cp

# Skyze libraries - Test Case Specific
from Skyze_Market_Data_Updater_Service.ExchangeCCXT import *
from Skyze_Messaging_Service.SkyzeMessageBusService import *


class ExchangeCCXT_test(UnitTestSkyzeAbstract):
  """Test the Bitfinex Class"""

  _package_name = "Skyze_Market_Data_Updater_Service"
  _class_tested = "ExchangeCCXT"

  @unittest.skip("Working on new test")
  def test_cctx(self):
    print("yup test_cctx")
    hitbtc = ccxt.hitbtc({'verbose': True})
    bitmex = ccxt.bitmex()
    huobi = ccxt.huobi()
    exmo = ccxt.exmo({
        'apiKey': 'YOUR_PUBLIC_API_KEY',
        'secret': 'YOUR_SECRET_PRIVATE_KEY',
    })

    hitbtc_markets = hitbtc.load_markets()

    print(hitbtc.id, hitbtc_markets)
    print(bitmex.id, bitmex.load_markets())
    print(huobi.id, huobi.load_markets())

    print(hitbtc.fetch_order_book(hitbtc.symbols[0]))
    print(bitmex.fetch_ticker('BTC/USD'))
    print(huobi.fetch_trades('LTC/CNY'))

  @unittest.skip("Working on new test")
  def test_getAllMarkets(self):
    exchangeBroker = ExchangeCCXT()
    exchangeBroker.getAllMarkets()

  def test_updateMarketData(self):
    # Set up for testing
    logger_class_name = self.__class__.__name__
    logger = SkyzeLogger(logger_class_name, "")
    log_message = f"{logger_class_name}::__init__::Started"

    message_bus = SkyzeMessageBusService()
    # Testing
    exchangeBroker = ExchangeCCXT(logger=logger, message_bus=message_bus)
    print("Start")
    print(cp.openingTitles())
    exchangeBroker.updateMarketData()


if __name__ == '__main__':
  unittest.main()

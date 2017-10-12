"""Created on 05/09/2017
   @author: michaelnew"""

# 3rd Party

# Our libraries - Required
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import

# Skyze imports
from Skyze_Messaging.Messages.MessageDataReceived import MessageDataReceived


class MessageDataReceived_test(UnitTestSkyzeAbstract):
    """Test class for the MessageDataReceived strategy"""

    def test_set_up(self):
        """ Tests object creation and getters"""

        # Test Data
        exchange = "Cryptopia"
        market_pair = "BTC_USDT"
        interval = "5_min"

        # Create the message
        msg = MessageDataReceived(exchange, market_pair, interval)

        # Output the Test ouput data
        print("=== JSON === === === === === ")
        print(msg.getJSON())

        # Assert by series
        assert(exchange == msg.getExchange())
        assert(market_pair == msg.getMarketPair())
        assert(interval == msg.getInterval())
        print("=== Assertions Passed === === === === === ")


if __name__ == '__main__':
    unittest.main()

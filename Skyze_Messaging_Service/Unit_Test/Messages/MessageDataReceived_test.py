"""Created on 05/09/2017
   @author: michaelnew"""

# 3rd Party

# Our libraries - Required
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import

# Skyze imports
from Skyze_Messaging.Messages.MessageDataReceived import MessageDataReceived
from Skyze_Messaging.Messages.SkyzeMessageTypes import *


class MessageDataReceived_test(UnitTestSkyzeAbstract):
    """Test class for the MessageDataReceived strategy"""

    def test_set_up(self):
        """ Tests object creation and getters"""

        # Test Data
        exchange = "Cryptopia"
        market_pair = "BTC_USDT"
        interval = "5_min"
        message_type = str(SkyzeMessageType.NEW_MARKET_DATA)

        # Create the message
        msg = MessageDataReceived(exchange, market_pair, interval)

        # Output the Test ouput data
        print("=== JSON === === === === === ")
        print(msg.getJSON())
        print("=== Message Type === === === === === ")
        print(msg.getMessageType())
        print(f"test data: {message_type}")

        # Assert by series
        assert(exchange == msg.getExchange())
        assert(market_pair == msg.getMarketPair())
        assert(interval == msg.getInterval())
        assert(message_type == msg.getMessageType())
        print("=== Assertions Passed === === === === === ")


if __name__ == '__main__':
    unittest.main()

"""Created on 08/09/2017
   @author: michaelnew"""

# Third Party Imports
import zmq

# Skyze Imports
from Skyze_Standard_Library.SkyzeServiceAbstract import *


class SkyzeScreenerService(SkyzeServiceAbstract):
    """Main Class for the Skyze Screener Service"""

    self.__running_screeners = []

    def __init__(self, message_bus):
        """Constructor"""
        super.__init__(self, message_bus)
        self.__connect_to_message_bus()
        self.__listen_to_message_bus()

    def getRunningScreeners(self):
        return self.__running_screeners

    def __connect_to_message_bus(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.setsockopt_string(zmq.SUBSCRIBE, '')
        socket.connect("tcp://127.0.0.1:4999")

    def __listen_to_message_bus(self):
        """Infinitely listens to the message bus
           routes messages to the appropriate Screener
           functions"""
        while True:
            msg = socket.recv_string()
            print(msg)
            if msg == "new data":
                self.__new_market_data_received(msg)

    def __new_market_data_received(self, msg):
        pass

"""Created on 08/09/2017
   @author: michaelnew"""

# Third Party Imports
import zmq

# Skyze Imports
from Skyze_Standard_Library.SkyzeServiceAbstract import *


class SkyzeScreenerService(SkyzeServiceAbstract):
    """Main Class for the Skyze Screener Service"""

    def __init__(self, message_bus):
        """Constructor"""
        super().__init__(message_bus)
        self.__running_screeners = []
        self.__connect_to_message_bus()
        # self.__listen_to_message_bus()

    def getRunningScreeners(self):
        return self.__running_screeners

    def __connect_to_message_bus(self):
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.SUB)
        self.__socket.setsockopt_string(zmq.SUBSCRIBE, '')
        self.__socket.connect("tcp://127.0.0.1:4999")

    def __listen_to_message_bus(self):
        """Infinitely listens to the message bus
           routes messages to the appropriate Screener
           functions"""
        while True:
            msg = self.__socket.recv_string()
            print(msg)
            if msg == "new data":
                self.__new_market_data_received(msg)

    def __new_market_data_received(self, msg):
        pass

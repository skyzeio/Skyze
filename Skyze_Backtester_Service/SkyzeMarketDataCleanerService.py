"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Back_Tester_Service import settings
from Skyze_Standard_Library.SkyzeServiceAbstract import *


class SkyzeBackTesterService(SkyzeServiceAbstract):
    """Skyze inter-service message logger"""

    def __init__(self, message_bus):
        """Constructor"""
        path_to_service = "Skyze_Back_Tester_Service"
        super().__init__(message_bus=message_bus, log_path=path_to_service)

    def receiveMessage(self, message_received):
        """Gets the mssage from the bus and routes internally"""
        # Parent class processing
        super().receiveMessage(message_received)
        # Route to appropriate service
        message_type = message_received.getMessageType()
        print("SkyzeBackTesterService::receiveMessage::NOT IMPLEMENTED")

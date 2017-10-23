"""Created on 16/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageServiceStatus(MessageSkyzeAbstract):
    """Service Status Message"""

    def __init__(self, service_name, service_status):
        """Constructor"""
        super().__init__(SkyzeMessageType.SERVICE_STATUS)
        self.__service = service_name
        self.__service_status = service_status
        self.__message_content = service_status

    def getService(self):
        """Getter"""
        return self.__service

    def getServiceStatus(self):
        """Getter"""
        return self.__service_status

    def getMessageContent(self):
        """Getter"""
        return self.__message_content

    def getJSON(self):
        """Getter example"""
        return super().getJSON() \
            + ', "service": "' + self.__service \
            + '", "service_status": "' + self.__service_status \
            + '"}'

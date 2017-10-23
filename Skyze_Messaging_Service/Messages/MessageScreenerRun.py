"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageScreenerRun(MessageSkyzeAbstract):
    """Run a specific screener"""

    def __init__(self, screener_name):
        """Constructor"""
        super().__init__(SkyzeMessageType.SCREENER_RUN)
        self.__screener_name = screener_name
        self.__message_content = f"{screener_name}"

    def getScreenerName(self):
        """Getter"""
        return self.__screener_name

    def getMessageContent(self):
        """Getter"""
        return self.__message_content

    def getJSON(self):
        """Return object as JSON"""
        text = super().getJSON()
        text += f', "screener name": "{self.__screener_name}"'
        text += f'}'
        return text

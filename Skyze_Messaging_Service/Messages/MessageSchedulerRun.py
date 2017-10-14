"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports

# Skyze Imports
from Skyze_Messaging_Service.Messages.MessageSkyzeAbstract import *


class MessageSchedulerRun(MessageSkyzeAbstract):
    """Prompts scheduler to run"""

    def __init__(self):
        """Constructor"""
        super().__init__(SkyzeMessageType.SCHEDULER_RUN)
        self.__message_content = "Scheduler Run"

    def getMessageContent(self):
        """Getter"""
        return self.__message_content

"""Created on 13/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json

# Skyze Imports
from Skyze_Notifier_Service import settings
from Skyze_Standard_Library.SkyzeServiceAbstract import *
# Skyze Messages
from Skyze_Messaging_Service.Messages.SkyzeMessageTypes import *
from Skyze_Messaging_Service.Messages.MessageMarketDataUpdaterRunComplete \
    import MessageMarketDataUpdaterRunComplete


class SkyzeNotifierService(SkyzeServiceAbstract):
    """Skyze inter-service message logger"""

    def __init__(self, message_bus):
        """Constructor"""
        path_to_service = "Skyze_Notifier_Service"
        super().__init__(message_bus=message_bus, log_path=path_to_service)

    def __sendEmail(self, msg_subject, msg_content):
        log_msg = f"{self.getType()}::sendEmail::NOT IMPLIMENTED::{msg_subject}\n{msg_content}"
        self._logger.log_info(log_msg)
        pass

    def __sendTweet(self, msg_subject, msg_content):
        log_msg = f"{self.getType()}::sendTweet::NOT IMPLIMENTED::{msg_content}"
        self._logger.log_info(log_msg)
        pass

    def __sendSMS(self, msg_subject, msg_content):
        self.__sendTweet(msg_subject, msg_content)

    def receiveMessage(self, message_received):
        """Gets the mssage from the bus and routes internally"""
        # Parent class processing
        super().__init__(message_received)
        # Route to appropriate service
        message_type = message_received.getMessageType()
        if message_type == SkyzeMessageType.NOTIFICATION:
            pass
        elif message_type == SkyzeMessageType.MARKET_DATA_UPDATER_RUN_COMPLETE:
            # TODO check user notification settings thensend apprpriately
            msg_subject = "Mkt Data Update Complete: " \
                + message_received.getMessageContent()
            msg_content = msg_subject
            self.__sendEmail(msg_subject, msg_content)
            self.__sendSMS(msg_subject, msg_content)
        else:
            self._unknownMessageTypeError(message_received)

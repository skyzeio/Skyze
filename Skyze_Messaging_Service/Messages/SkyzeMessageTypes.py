"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from enum import Enum

# All messages types that can be sent by skyze services
SkyzeMessageType = Enum("MessageType",
                        "NEW_MARKET_DATA \
                        SCREENER_RUN \
                        MARKET_DATA_UPDATER_RUN \
                        MARKET_DATA_UPDATER_RUN_ALL \
                        MARKET_DATA_UPDATER_RUN_COMPLETE \
                        NOTIFICATION \
                        SCHEDULER_RUN \
                        SCHEDULER_TEST SIGNAL \
                        SERVICE_STATUS")

# Future order types: ORDER FILL SENTIMENT NULL

"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from enum import Enum


SkyzeMessageType = Enum("MessageType",
                        "NEW_MARKET_DATA SCREENER_RUN MARKET_DATA_UPDATER_RUN \
                        MARKET_DATA_UPDATER_RUN_ALL NOTIFICATION SCHEDULER_RUN \
                        SIGNAL ORDER FILL SENTIMENT NULL")

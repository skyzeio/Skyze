"""Created on 13/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json

# Skyze Imports
from Skyze_Standard_Library.SkyzeServiceAbstract import *


class SkyzeNotifierService(SkyzeServiceAbstract):
    """Skyze inter-service message logger"""

    def __init__(self, message_bus):
        """Constructor"""
        path_to_service = "Skyze_Notifier_Service"
        super().__init__(message_bus=message_bus, log_path=path_to_service)

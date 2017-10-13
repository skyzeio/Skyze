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
        super().__init__(message_bus)

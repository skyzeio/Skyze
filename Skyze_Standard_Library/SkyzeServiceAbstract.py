"""Created on 12/10/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json

# Skyze Imports
import ExceptionSkyzeAbstract


class SkyzeServiceAbstract(object):
    """Skyze Base class for services"""

    def __init__(self, message_bus=None):
        """Constructor"""
        self.__created = datetime.now()
        self.__message_bus = message_bus
        print(f"Log: {self.getType()} Started")

    def getType(self):
        return self.__class__.__name__

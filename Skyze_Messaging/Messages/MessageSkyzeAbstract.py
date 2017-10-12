"""Created on 08/09/2017
   @author: michaelnew"""

# Third Party Imports
from datetime import datetime
import json

# Skyze Imports
import ExceptionSkyzeAbstract


class MessageSkyzeAbstract(object):
    """Skyze inter-service messages"""

    def __init__(self):
        """Constructor"""
        self.__created = str(datetime.now())

    def getCreated(self):
        """Getter"""
        return self.__created

    def getJSON(self):
        """Getter"""
        return "PARENT get JSON"

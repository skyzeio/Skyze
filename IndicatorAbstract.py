"""Created on 08/09/2017
@author: michaelnew"""


import Skyze_Standard_Library.settings_skyze as settings_skyze
from datetime import datetime


class IndicatorAbstract(object):
    """Class Docs"""

    def __init__(self):
        """Constructor"""

    def _saveToExcel(self, df, path, append_date=True):
        # Construct the file name
        file_name = path + '/' + self._name
        if append_date:
            file_name += "-" + str(datetime.now())
        file_name += '.xlsx'
        # Save to excel
        df.to_excel(file_name, index=True)

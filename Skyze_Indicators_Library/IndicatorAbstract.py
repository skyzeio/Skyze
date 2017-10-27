"""Created on 08/09/2017
@author: michaelnew"""


class IndicatorAbstract(object):
    """Class Docs"""

    def __init__(self):
        """Constructor"""

    def _saveToExcel(self, df, append_date=True):
        # Construct the file name
        file_name = settings_skyze.results_file_path + '/' + self._name
        if append_date:
            file_name += "-" + str(datetime.now())
        file_name += '.xlsx'
        # Save to excel
        df.to_excel(file_name, index=True)

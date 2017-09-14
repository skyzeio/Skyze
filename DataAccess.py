#----------------------------------------------------------------------------------------------------------
#
#   CLASS DataAccess
#
#----------------------------------------------------------------------------------------------------------

import os
import settings


class DataAccess:


    def __init__(self):
        Data = []
        
    
    # creates the full path and file name
    
    def fileName( self, p_market_name, p_extension ):
        return os.path.join(settings.data_file_path, "%(name)s.%(extension)s" % {"name":p_market_name, "extension":p_extension})
    
    
       
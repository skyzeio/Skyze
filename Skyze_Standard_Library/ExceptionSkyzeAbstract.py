'''
Created on 09/09/2017

@author: michaelnew
'''

# 3rd party libraries
from inspect import trace
import inspect
import sys
from pprint import pprint
import json


class ExceptionSkyzeAbstract(Exception):
    '''
    classdocs
    '''
# 
# 
#     def __init__(self):
#         '''
#         Constructor
#         '''
#         pass
        
    def printException(self, p_line_no, p_message):  
        trace_len = len(trace())
        err_msg = "\nSKYZE EXCEPTION: " + self.__class__.__name__
        err_msg += "::" + trace()[0].function
        err_msg += "::" + str(trace()[0].lineno)
        err_msg += "\n Called: " + trace()[trace_len-1].function
        err_msg += "   on line: " + str(trace()[trace_len-1].lineno)
        err_msg += "\n code Context: " + str(trace()[trace_len-1].code_context)
        err_msg += "\n ...." + p_message + "  ... " + str(sys.exc_info()[0])
        err_msg += "\n LOCALS ...." + str(sys.exc_info()[2].tb_frame.f_locals)
#         pprint(str(sys.exc_info()[2].tb_frame.f_locals))
#         print(json.dumps(sys.exc_info()[2].tb_frame.f_locals, indent=4))
        print(err_msg)
        print(); print(); print()
               
               
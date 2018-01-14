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
import rollbar

# Skyze Imports
from Skyze_Standard_Library.SkyzeLogger import *


class ExceptionSkyzeAbstract(Exception):
    """classdocs"""
#
#
#     def __init__(self):
#         '''
#         Constructor
#         '''
#         pass

    def reportException(self, class_name, p_line_no, p_message, logger, to_print=True, to_raise=True):
        trace_len = len(trace())
        err_msg = "\nSKYZE EXCEPTION: " + class_name
        err_msg += "::" + trace()[1].function
        err_msg += "::" + str(trace()[1].lineno)
        err_msg += "\n Called: " + trace()[trace_len - 1].function
        err_msg += "   on line: " + str(trace()[trace_len - 1].lineno)
        err_msg += "\n code Context: " + \
            str(trace()[trace_len - 1].code_context)
        err_msg += "\n ...." + p_message + "  ... " + str(sys.exc_info()[0])
        err_msg += "\n LOCALS ...." + str(sys.exc_info()[2].tb_frame.f_locals)
#         pprint(str(sys.exc_info()[2].tb_frame.f_locals))
#         print(json.dumps(sys.exc_info()[2].tb_frame.f_locals, indent=4))

        # Log it
        log_message = f"{class_name}: : reportException: : exception created\n{err_msg}"
        logger.log_info(log_message, to_print)

        # Rollbar it
        rollbar_on = True
        if rollbar_on:
            rollbar.init('8f67acbc427a4d6ba80c31516bd355da',
                         'Mike Laptop')  # access_token, environment
            rollbar.report_message(log_message)

        if to_raise:
            raise self

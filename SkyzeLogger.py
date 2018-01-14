"""Created on 16/10/2017
   @author: michaelnew"""

# Third Party Imports
import logging

# Skyze Imports
import Skyze_Standard_Library.ExceptionSkyzeAbstract


class SkyzeLogger(object):
    """Skyze direct logging. It is a wrapper around the python Logger"""

    def __init__(self, logger_name, log_path=""):
        """Constructor
            From https://stackoverflow.com/questions/17035077/python-logging-to-multiple-log-files-from-different-classes"""
        # Construct the log name and path
        if log_path != "":
            log_path = log_path + "/"
        log_file = f'{log_path}Logs/Skyze_Log_{logger_name}.log'
        level = logging.INFO

        # Set up logger
        self._logger = logging.getLogger(logger_name)
        formatter = logging.Formatter('%(asctime)s : %(message)s')
        fileHandler = logging.FileHandler(log_file, mode='a')
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        self._logger.setLevel(level)
        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

    def log_info(self, log_message, print_log=True):
        if print_log:
            print(f"{log_message}")
        self._logger.info(f"Log: {log_message}")

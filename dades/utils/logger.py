# --------------------------------
# Author : Garvey Ding
# Create : 2018-10-24
# Modify : 2018-10-24 by Garvey
# --------------------------------

import json
import logging
import os.path
import sys

from config import ConfigLogger


class BaseLogger(object):

    def __init__(self, name = None):
        self.name = name or __name__
        # self.logging_format = "%(asctime)s.%(msecs)03d %(levelname)s [%(name)s]: %(message)s"
        self.logging_format = "%(asctime)s %(levelname)s [%(name)s]: %(message)s"
        self.date_format = "%Y-%m-%d %H:%M:%S"
        self.level = logging.INFO

        self.filename = None
        if ConfigLogger.to_file:
            if not os.path.exists(ConfigLogger.log_path):
                os.makedirs(ConfigLogger.log_path)
            self.filename = os.path.join(ConfigLogger.log_path, ConfigLogger.log_file)
        

        self.logger = self.get_logger()

    def get_logger(self):
        if ConfigLogger.to_file:
            logging.basicConfig(
                filename = self.filename, 
                format = self.logging_format, 
                datefmt = self.date_format
            )

        else:
            stdout_handler = logging.StreamHandler(sys.stdout)
            logging.basicConfig(
                format = self.logging_format, 
                datefmt = self.date_format,
                handlers = [stdout_handler,]
            )

        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)

        return logger

    def log(self, msg):
        if self.level == logging.WARNING:
            self.logger.warning(msg)
        elif self.level == logging.DEBUG:
            self.logger.debug(msg)
        elif self.level == logging.ERROR:
            self.logger.error(msg)
        else: 
            self.logger.info(msg)

    def set_level_error(self):
        self.level = logging.ERROR

    def set_level_info(self):
        self.level = logging.INFO

    def errlog(self, msg):
        self.set_level_error()
        self.log(msg)
        self.set_level_info()

    def log_to(self, msg, filename, level=logging.ERROR):
        handler = logging.FileHandler(filename, 'a')
        formatter = logging.Formatter(self.logging_format, self.date_format)
        handler.setFormatter(formatter)

        handler.setLevel(level)

        if isinstance(msg, dict):
            try:
                m = json.dumps(m)
            except:
                m = str(msg)
        else:
            m = str(msg)

        handler.stream.writelines(m + '\n')
        handler.stream.close()


class InfoLogger(BaseLogger):

    def __init__(self, name = None):
        super(InfoLogger, self).__init__(name = name)
        self.level = logging.INFO


class DebugLogger(BaseLogger):

    def __init__(self, name = None):
        super(DebugLogger, self).__init__(name = name)
        self.level = logging.DEBUG


class WarningLogger(BaseLogger):

    def __init__(self, name = None):
        super(WarningLogger, self).__init__(name = name)
        self.level = logging.WARNING


class Logger(BaseLogger):

    def __init__(self, name = None):
        super(Logger, self).__init__(name = name)



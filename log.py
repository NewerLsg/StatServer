# -*- coding: utf-8 -*-
import glob
import logging
import logging.handlers

LOG_FILENAME = 'log/server.log'

# Set up a specific logger with our desired output level
serverLog = logging.getLogger('MyLogger')
serverLog.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=1024*1024, backupCount=5)

fileFormat = logging.Formatter('%(asctime)s  %(message)s','%a, %d %b %Y %H:%M:%S')

handler.setFormatter(fileFormat)

serverLog.addHandler(handler)
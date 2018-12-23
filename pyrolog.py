#!/usr/bin/env python3

import logging
import time
import sys
 
from logging.handlers import TimedRotatingFileHandler
 
LOGGING_MSG_FORMAT = '%(asctime)s %(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def createLogger(path):
  logger = logging.getLogger("pyrolog")
  logger.setLevel(logging.INFO)
  handler = TimedRotatingFileHandler(path,
                                     when="midnight",
                                     interval=1,
                                     backupCount=30)
  handler.setFormatter(logging.Formatter(fmt=LOGGING_MSG_FORMAT, datefmt=LOGGING_DATE_FORMAT))
  logger.addHandler(handler)
  return logger
 
if __name__ == "__main__":
  logFile = sys.argv[1]
  logger = createLogger(logFile)
  for line in sys.stdin:
    logger.info(line.strip())

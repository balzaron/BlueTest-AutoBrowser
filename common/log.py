import inspect
import logging
import os
import time
from logging.handlers import RotatingFileHandler
from common.config_center import globalconfig

logConf:dict = globalconfig().get('log')
filepath = logConf.get('path')
fn = logConf.get('filename')
sn = logConf.get('screenname')
fileSize = int(logConf.get('filesize'))
maxFileNum = int(logConf.get('maxfilenum'))
logfile = filepath+fn

baseLogPath = filepath
errPath = logConf.get('errPath')


# rotateHandler = RotatingFileHandler(logfile, maxBytes= fileSize *1024 *1024, backupCount=maxFileNum)
#
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=(rotateHandler,
#               logging.StreamHandler())
#               # logging.FileHandler(baseLogPath),
#               # logging.FileHandler(baseLogPath+errPath),
#               # logging.FileHandler(baseLogPath+criticalPath))
# )
#
#
#
logger = logging.getLogger()

#===================================================================================================



handlers = {logging.NOTSET: "/tmp/logs/MioLog-notset.log",
            logging.DEBUG: "/tmp/logs/MioLog-debug.log",
            logging.INFO: "/tmp/logs/MioLog-info.log",
            logging.WARNING: "/tmp/logs/MioLog-warning.log",
            logging.ERROR: "/tmp/logs/errors/MioLog-error.log",
            logging.CRITICAL: "/tmp/logs/critical/MioLog-critical.log"}

for path in handlers.values():
    p = path.split('MioLog-')[0]
    if not os.path.exists(p):
        os.makedirs(p)
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.close()

def createHandlers():
    logLevels = handlers.keys()
    for level in logLevels:
        path = os.path.abspath(handlers[level])
        handlers[level] = logging.FileHandler(path)


# 加载模块时创建全局变量
createHandlers()


class miologging(object):
    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __init__(self, level=logging.NOTSET):
        self.__loggers = {}
        logLevels = handlers.keys()

        for level in logLevels:
            logger = logging.getLogger(str(level))
            logger.addHandler(handlers[level])
            logger.setLevel(level)
            self.__loggers.update({level: logger})

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]
        '''日志格式：[时间] [类型] [记录代码] 信息'''
        return "[%s - %s] %s" % (lineNo, functionName, message)

    def info(self, message):
        message = self.getLogMessage("info", message)
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)
        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)
        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)
        self.__loggers[logging.CRITICAL].critical(message)
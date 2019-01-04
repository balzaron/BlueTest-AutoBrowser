# encode=utf-8
import sys

from loguru import logger
import os
from mioAuto import logPath
__logConfig= dict(
    rotation='50MB',
    enqueue=True,
    # colorize=True,
    # format="<green>{time}</green> <level>{message}</level>",
    encoding='utf-8',
    format="{level} {time} {message}"
)
fp = logPath or '/tmp/logs/'
if not os.path.exists(fp):
    os.makedirs(fp, exist_ok=True)

fp = fp+'mioauto_{time}.log'

logger.add(fp, **__logConfig)
logger.start(sys.stderr, format="{level} {time} {message}", filter="my_module", level="INFO")

logger.error('this is so easy')
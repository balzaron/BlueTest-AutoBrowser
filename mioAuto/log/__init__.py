# encode=utf-8
from loguru import logger

__logConfig= dict(
    rotation='1KB',
    enqueue=True,
    # colorize=True,
    # format="<green>{time}</green> <level>{message}</level>",
    encoding='utf-8',
)
fp = '/Users/miotech/opt/name_{time}.log'

logger.add(fp, **__logConfig)

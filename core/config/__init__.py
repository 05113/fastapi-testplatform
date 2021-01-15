import os
from common import logger
env = os.getenv("ENV","")
if env:
    logger.info("---生产环境启动---")
    pass
else:
    logger.info("---开发环境启动---")
    from .development_config import settings

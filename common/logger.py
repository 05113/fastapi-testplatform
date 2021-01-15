from loguru import logger
import os
import time

# 获取目录:
# os.path.abspath(__file__):获取该文件的绝对路径
# os.path.dirname:获取该文件的父路径
__basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 组装路径:

__log_path = os.path.join(__basedir,"logs")

if not os.path.exists(__log_path):
    os.mkdir(__log_path)
__log_debug_path = os.path.join(__log_path,"log_{time}.log")

# loguru自带配置
# rotation:rotation="500 MB" 每 500MB 存储一个文件，每个 log 文件过大就会新创建一个 log 文件
#         :rotation='00:00' 每天 0 点新创建一个 log 文件输出
#         :rotation='1 week'每周创建
# retention:retention='10 days' log 文件里面就会保留最新 10 天的 log
# compression:compression='.zip' 配置文件的压缩格式，比如使用 zip 文件格式保存
logger.add(__log_debug_path,rotation="00:00",retention="10 days",compression='.zip',enqueue=True,encoding="utf-8")

# 参数化
# logger.info('If you are using Python {}, prefer {feature} of course!', 3.6, feature='f-strings')

__all__ = ['logger']


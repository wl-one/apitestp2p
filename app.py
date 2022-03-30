import logging  # 导入logging日志类
import time
from logging import handlers
import os

# 当前的目录结构
# os.path.abspath(__file__)指的是当前模块的绝对路径，os.path.dirname(path)返回路径为 path 的目录名称
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 初始化日志配置
def init_config():
    # 初始化日志对象，设置日志级别
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 创建控制台日志处理器和文件日志处理器
    sh = logging.StreamHandler()
    # 使用相对路径；os.sep的意思是不知道\/的时候直接用这个；fh即filehandler的缩写
    # 注意strftime里面的日期大小写
    logfile = BASE_DIR + os.sep + "log" + os.sep + "log-{}.log".format(time.strftime('%Y%m%d-%H%M%S'))
    fh = logging.handlers.TimedRotatingFileHandler(logfile, when='M', interval=5, backupCount=5, encoding='utf-8')
    # 设置日志格式，创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器设置到日志处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)

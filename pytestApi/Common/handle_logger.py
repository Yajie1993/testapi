'''
日志模块封装
'''
import logging
from Common.handle_path import logs_dir
from Common.handle_config import conf

class HandleLogger(logging.Logger):

    def __init__(self,name,level=logging.INFO,file=None):
        # 设置输出级别、输出格式、输出渠道
        super().__init__(name,level)

        #日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)d line %(message)s'
        formatter = logging.Formatter(fmt)

        # 控制台输出渠道
        handle = logging.StreamHandler()
        handle.setFormatter(formatter)
        self.addHandler(handle)

        # 文件输出渠道
        if file:
            handle1 = logging.FileHandler(file,encoding="utf-8")
            handle1.setFormatter(formatter)
            self.addHandler(handle1)

#是否写入日志
if conf.getboolean("logs","file_ok"):
    file_name = (logs_dir + conf.get("logs", "file_name"))
else:
    file_name = None

logger = HandleLogger(conf.get("logs","name"),conf.get("logs","level"),file=file_name)

if __name__ == '__main__':
    logger.info("ceshi")
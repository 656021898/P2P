# -*_ coding:utf-8 _*-
import logging
import os
from common.GetPath import GetPath


# my_logger = logging.getLogger("python11")
# my_logger.setLevel("DEBUG")
#
# #设定格式
# formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
#
# #创建一个输出到控制台的渠道
# ch = logging.StreamHandler()
# ch.setLevel("DEBUG")#设定输入的级别
# ch.setFormatter(formatter)
#
# #创建一个输出到文件的渠道
# fh = logging.FileHandler(os.path.join(GetPath.get_path() ,"test_result" ,"test_logging.txt") ,encoding="utf-8")
# fh.setLevel("DEBUG")#设定输入的级别
# fh.setFormatter(formatter)
#
# #两者对接
# my_logger.addHandler(ch)
# my_logger.addHandler(fh)
#
# my_logger.debug("sjlfjldsjf ")

class MyLog:
    def my_log(self,leavl,msg):
        my_logger = logging.getLogger("开发者")
        my_logger.setLevel(leavl)
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(leavl)
        ch.setFormatter(formatter)

        fh = logging.FileHandler(os.path.join(GetPath.get_path() ,"test_result" ,"test_logging.txt") ,encoding="utf-8")
        fh.setLevel(leavl)
        fh.setFormatter(formatter)

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        try:
            assert leavl == "AA"
            if leavl == "DEBUG":
                my_logger.debug(msg)
            elif leavl == "INFO":
                my_logger.info(msg)
            elif leavl == "WARNING":
                my_logger.warning(msg)
            elif leavl == "ERROR":
                my_logger.error(msg, exc_info=1)
            elif leavl == "CRITICAL":
                my_logger.critical(msg)
            elif leavl == "EXCEPT":
                my_logger.exception(msg)
        except AssertionError as e:
            my_logger.exception(msg)

        #每次用完都要关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log("DEBUG",msg)

    def info(self,msg):
        self.my_log("INFO",msg)

    def warning(self,msg):
        self.my_log("ERROR",msg)

    def error(self,msg):
        self.my_log("WARNING",msg)

    def critical(self,msg):
        self.my_log("CRITICAL",msg)

    def exception(self,msg):
        self.my_log("EXCEPT",msg)

if __name__ == "__main__":
    MyLog().exception("123123123213")


# -*_ coding:utf-8 _*-

import configparser
import os
from common.GetPath import GetPath

class ReadConfig:

    def __init__(self,module,module_key):
        self.module = module
        self.module_key = module_key

    def readConfig(self):
        cf = configparser.ConfigParser()
        cf.read(filenames=os.path.join(GetPath.get_path(), "conf/case.config"), encoding="utf-8")
        return cf[self.module][self.module_key]



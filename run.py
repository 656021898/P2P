# -*_ coding:utf-8 _*-
# -*_ coding:utf-8 _*-
import unittest
from common.HTTPTestCase import HttpTestCase_ddt
import configparser
import HTMLTestRunnerNew
from common.GetPath import GetPath
import os

cf = configparser.ConfigParser()
cf.read(filenames=os.path.join(GetPath.get_path(),"conf/case.config"),encoding="utf-8")
print(os.path.join(GetPath.get_path(),"/conf/case.config"))

suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(HttpTestCase_ddt))
with open(cf["report"]["htmlReport"], 'wb') as myfile:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=myfile,title='My unit test',description='hahah')
    runner.run(suite)



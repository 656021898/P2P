# -*_ coding:utf-8 _*-
import unittest
import ddt
import os
import logging
from common.DoExcel import DoExcel
from common.TestHttpRequest import TestHttpRequest
from common.GetCookie import GetCookie
from common.GetPath import GetPath
from common.GetMobile import GetMobile
from common.ReadConfig import ReadConfig
from common.my_log import MyLog


# 获取测试数据
test_data = DoExcel().read_excel(
    ExcelReadName=os.path.join(GetPath.get_path(), ReadConfig("Excel","ExcelReadName").readConfig()),
    SheetReadName=ReadConfig("Excel","SheetReadName").readConfig())


#测试类
@ddt.ddt
class HttpTestCase_ddt(unittest.TestCase):

    my_logger = logging.getLogger("python11")
    my_logger.setLevel("NOTSET")
    ch = logging.StreamHandler()
    ch.setLevel("NOTSET")
    fh = logging.FileHandler(os.path.join(GetPath.get_path(),"test_result","test_logging.txt"),encoding="utf-8")
    fh.setLevel("NOTSET")
    my_logger.addHandler(ch)
    my_logger.addFilter(fh)


    @ddt.data(*test_data)
    def test_http_case(self,item):
        Write_list = []
        Excel_dict = {}
        if eval(item["data"])["mobilephone"] == "${tel}":
            item = GetMobile().getMobile(item)
        res = TestHttpRequest(url=(item["host"] + item["url"]), data=eval(item["data"]),
                              method=item["method"],cookie=getattr(GetCookie,"COOKIE")).HttpRequest()
        if res.cookies:
            setattr(GetCookie,"COOKIE",res.cookies)
        try:
            self.assertEqual(str(item["code"]),res.json()["code"])
            Excel_dict["TestResult"] = "通过"
        except (AssertionError,Exception) as e:
            Excel_dict["TestResult"] = "未通过"
            MyLog().exception("dhfksfhdksjhf")
            raise Exception("用例执行未通过，错误是：{}".format(e))
        finally:
            Excel_dict["id"] = item["id"]
            Excel_dict["res_json"] = str(res.json())
            Excel_dict["real_code"] = res.json()["code"]
        #获取所有Case执行结果的list，格式为list=[{},{}]
            Write_list.append(Excel_dict)
            # 把测试结果写到测试用例的后面
            DoExcel().write_excel(ExcelWriteName=os.path.join(GetPath.get_path(),ReadConfig("Excel","ExcelReadName").readConfig()),
                                  SheetWriteName=ReadConfig("Excel","SheetReadName").readConfig(),
                                  Excel_list=Write_list)

if __name__ == '__main__':
    unittest.main()


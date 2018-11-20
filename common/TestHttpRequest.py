import requests

class TestHttpRequest:
    def __init__(self,url,data,method,cookie=""):
        self.url = url
        self.data = data
        self.method = str(method).lower()
        # self.code = code
        self.cookie = cookie

    def HttpRequest(self):
        if self.method == "post":
            res = requests.post(url=self.url,data=self.data,cookies=self.cookie)
        elif self.method == "get":
            res = requests.get(url=self.url, params=self.data, cookies=self.cookie)
        else:
            print("请输入正确的method")
        return res


if __name__ == "__main__":
    res = TestHttpRequest(url="http://47.107.168.87:8080/futureloan/mvc/api/member/login",data={"mobilephone":"18544444402","pwd":"123456"},method="post").HttpRequest()
    cookie = res.cookies
    print(cookie)
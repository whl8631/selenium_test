# coding=utf-8
from time import sleep

import yaml
from selenium import webdriver


class TestCookieLogin():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_get_cookies(self):
        # 1。访问企业微信主页/登陆页面
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        self.driver.get("https://dev.halo.360.net:18100/emc/login")
        # 2。等待20s人工扫码操作
        sleep(20)
        # 3。等成功登陆之后，再去获取cookie信息
        cookie = self.driver.get_cookies()
        print(cookie)
        # 4。将cookie存入一个可持久存储的地方。文件
        # 打开文件的时候添加写入权限
        with open("cookie.yaml","w") as f:
            # 第一个参数是要可入的数据
            yaml.safe_dump(cookie,f)

    def test_add_cookie(self):
        # 1.访问企业微信主页面
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        self.driver.get("https://dev.halo.360.net:18100/emc/login")
        # 2。定义cookie.，cookie信息从文件中获取
        cookie = yaml.safe_load(open("cookie.yaml"))
        # 3.植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        sleep(3)
        # 4.再次访问企业微信页面，发现无需扫码自动登陆
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        self.driver.get("https://dev.halo.360.net:18100/emc/login")
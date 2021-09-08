# ！/usr/bin/env python
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogWarts:
    def setup(self):
        # 初始化driver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  # 隐式等待
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        # 关闭driver
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID,"kw").send_keys("霍格沃滋测试学院")
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()
        self.driver.find_element(By.LINK_TEXT,"霍格沃兹测试学院 - 主页")
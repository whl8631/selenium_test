# coding=utf-8
from time import sleep

from test_selenium.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id('stfile').send_keys("/Users/wangliang/seleniumTest/Test_no1/test_selenium/image/test.png")
        sleep(3)
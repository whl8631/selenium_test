# coding=utf-8
from time import sleep
from test_selenium.base import Base


class TestWindows_Handle(Base):
    def test_windows_handle(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('s-top-loginbtn').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('123145678901')
        sleep(3)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()

        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('ueername')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()

        sleep(3)
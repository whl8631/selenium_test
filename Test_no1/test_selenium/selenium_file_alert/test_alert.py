# coding=utf-8
from time import sleep
from selenium.webdriver import ActionChains
from test_selenium.base import Base


class TestAlert(Base):
    def test_alert(self):
        """
        打开网页
        操作窗口右侧页面，将元素1拖拽到元素2
        会出现一个alert弹框，点击弹框中的确定
        然后再按"点击运行"
        关闭网页
        :return:
        """
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")

        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        sleep(2)
        print("点击alert 确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to_default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)


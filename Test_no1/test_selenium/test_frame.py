# coding=utf-8
from test_selenium.base import Base

class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        draggable = self.driver.find_element_by_id("draggable").text
        print(draggable)
        # # 方法1
        # self.driver.switch_to.parent_frame()
        # 方法2
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
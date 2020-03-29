from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Base_Page.BasicConfig import BaseConfig


class SearchPage(BaseConfig):    # 重构过来的 表示'搜索页'
    _input_locator = (By.ID, "com.xueqiu.android:id/search_input_text")
    _name_locator = (By.ID, "name")

    def search(self, keyword):       # 搜索 'ketword' ，参数执行的时候 传进去就行
        self.find_element(self._input_locator).send_keys(keyword)      ## 使用了 BaseConfig 中的封装方法
        self.find_element(self._name_locator).click()

        # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        # self.driver.find_element_by_id("name").click()

        return self

    def get_current_price(self):
        return float(self.driver.find_element_by_id("current_price").text)     # 强制转换成 float 类型
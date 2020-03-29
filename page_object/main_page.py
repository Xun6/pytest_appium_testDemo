from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Base_Page.BasicConfig import BaseConfig
from page_object.po_dome import SearchPage


class MainPage(BaseConfig):      #重构过来的 一个主页      把 BaseConfig 中封装的方法引用过来

    _search_locator = (By.ID, "com.xueqiu.android:id/home_search")     # 表示私有属性
    def to_search(self):
        print("click")
        self.find_element(self._search_locator).click()        ## 使用了 BaseConfig 内封装的通用方法

        # self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        return SearchPage(self.driver)     # 返回搜索页 （表示上方 点击操作后 会进入一个搜索页面,传递一个 self.drvier）
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.po_dome import SearchPage


class MainPage(object):      #重构过来的 一个主页
    def __init__(self, driver: WebDriver):    # 引入一个 driver参数，并赋予类型 WebDriver
        self.driver=driver


    def to_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        return SearchPage(self.driver)     # 返回搜索页 （表示上方 点击操作后 会进入一个搜索页面,传递一个 self.drvier）
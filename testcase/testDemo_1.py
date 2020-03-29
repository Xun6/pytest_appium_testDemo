from time import sleep

from appium import webdriver

from page_object.App import App
from page_object.po_dome import SearchPage

## 测试用例，调用各种封装的方法 完成运行
class TestCase:

    def setup(self):
       self.search_page = App.start().to_search()   #启动应用 进入首页 ，在进入搜索页   初始化一个变量 search_page


    def test_page_object(self):
        self.search_page.search("alibaba")      #调用 SearchPage 的 search() 方法 ，并给参数 keyword 传一个值 'alibaba'
        assert self.search_page.get_current_price() > 10    #断言

    def teardown(self):
        App.quit()    # 调用 App内的 quit（） 方法
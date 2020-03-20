class SearchPage(object):    # 重构过来的 表示'搜索页'
    def __init__(self, driver):
        self.driver=driver

    def search(self, keyword):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()

        return self

    def get_current_price(self):
        return float(self.driver.find_element_by_id("current_price").text)
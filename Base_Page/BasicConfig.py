from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BaseConfig:             # 对通用方法的封装
    ## 列出一个黑名单
    _black_list =[
        (By.ID, "image_cancel"),
        (By.ID, "tips")
    ]

    def __init__(self, driver: WebDriver):    # 对初始化的 一个封装
        self.driver = driver


    def find_element(self, locator):
        print(locator)     ##  打印
        try:
            return self.driver.find_element(*locator)       ## 若找到 直接返回该元素
        except:                      ## 捕获异常，若出现异常，进入一个异常处理逻辑
            self.handle_exception()
            return self.driver.find_element(*locator)    # 异常逻辑处理完，再次返回这个元素


    ## 独立的 弹窗（如：好评、升级更新、广告）处理逻辑
    def handle_exception(self):
        for locator in self._black_list:
            els = self.find_elements(*locator)
            if len(els) >= 1:       ## 判断如果找到该元素,点击她
                els[0].click()
            else:                  ## 否则就打印她
                print("%s not found" % str(locator))






















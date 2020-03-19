from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps["unicodeKeyboard"] =True    # 启用表示可以输入其他语言

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)        # 隐式等待   （这是一个全局设定）   (在服务端轮询的)

        # 显示等待（此方法可以去掉弹出的 升级提示弹窗）
        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        # )
        # self.driver.find_element_by_id("image_cancel").click()

    def test_demo(self):
        # sleep(15)
        # if len(self.driver.find_element_by_id("image_cancel")) >=1:
        #     self.driver.find_element_by_id("image_cancel").click()
        # else:
        #     pass
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el4.send_keys("alibaba")

    def test_unicodeKeyboard(self):
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el4.send_keys("阿里巴巴")

    def test_gsm_call(self):     # 设备交互 API 的使用
        self.driver.make_gsm_call('13617920171', GsmCallActions.CALL)
        self.driver.send_sms('13617920171', "Hello world!")

    def teardown(self):
        sleep(10)
        self.driver.quit()

    # if __name__ == "__main__":
    #     pytest.main(["-q","Demo_pytest.py"])


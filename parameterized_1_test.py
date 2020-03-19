from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    search_data=yaml.safe_load(open("search.yaml", "r"))   # 定义一个获取外部文件的变量
    print(search_data)
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "mumu"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # caps["unicodeKeyboard"] =True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(8)

        # 显示等待（此方法可以去掉 弹出的 升级提示弹窗）
        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        # )
        # self.driver.find_element_by_id("image_cancel").click()

    @pytest.mark.parametrize("keyword_1", search_data)   # 使用外部文件里的数据

    # 参数调用_2
    def test_parametrize_1_demo_fromsearch(self, keyword_1):
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el4.send_keys(keyword_1)
        sleep(2)

    def teardown(self):
        sleep(5)
        self.driver.quit()



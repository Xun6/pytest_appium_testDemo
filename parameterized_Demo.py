# coding=utf-8
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
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
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        )
        self.driver.find_element_by_id("image_cancel").click()

    @pytest.mark.parametrize("keyword", [
        ("alibaba"),
        ("pdd"),
        ("jd")
    ])
    def test_parametrize_demo(self, keyword):
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el4.send_keys(keyword)

    def teardown(self):
        self.driver.quit()

    # if __name__ == "__main__":    # 在python2.7下运行需要这条语句，但是切换到python3.7下运行就不需要这条语句了（亲测有效）
    #     pytest.main(["-q","parameterized_Demo.py"])


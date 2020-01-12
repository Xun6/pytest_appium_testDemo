# coding=utf-8
from time import sleep

from appium import webdriver
from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestDemo(TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "mumu"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(8)

        # 显示等待
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        )
        self.driver.find_element_by_id("image_cancel").click()

    def test_assert(self):
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el4.send_keys("alibaba")

        # assert "close" in self.driver.find_element_by_id("com.xueqiu.android:id/action_close").get_attribute("resource-id")

        # hamcrest 断言的应用
        assert_that(self.driver.find_element_by_id("com.xueqiu.android:id/action_close").get_attribute("text")), equal_to("取消")


    def tearDown(self):
        self.driver.quit()




# coding=utf-8
from time import sleep

from appium import webdriver
from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestApiDemo(TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "mumu"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(8)

    def test_toast(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));'
        ).click()  # 滑动界面至指定 位置（例如：text）
        self.driver.find_element_by_accessibility_id("Make a Popup!").click()
        self.driver.find_element_by_xpath("//*[@text='Search']").click()
        print (self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text)  # 打印出toast显示文本

    def tearDown(self):
        self.driver.quit()




# coding=utf-8
from time import sleep

from appium import webdriver
from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

        # 第一种等待方法
        # sleep(15)
        # self.driver.find_element_by_id("image_cancel").click()

        # 第二种等待方法
        # sleep(15)
        # if len(self.driver.find_element_by_id("image_cancel")) >=1:
        #     self.driver.find_element_by_id("image_cancel").click()

        # 显示等待
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        )
        self.driver.find_element_by_id("image_cancel").click()

        # 第三种等待方法
        # def loaded(driver):
        #     if len(self.driver.find_element_by_id("image_cancel")) >=1:
        #         self.driver.find_element_by_id("image_cancel").click()
        #         return True
        #     else:
        #         return False
        # 未找到报错，给抛出一个异常
        # try:
        #     WebDriverWait(self.driver, 15).until(loaded)
        # except:
        #     print("no uptate")

    def test_demo(self):
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el4.send_keys("alibaba")


     # xpath运用方法
    # def test_Xpath(self):
    #     self.driver.find_element_by_xpath("//*[@text='自选' and contains(@resource-id, 'tab_name')]").click()

    # def teat_performance(self):
    #     print (self.driver.get_performance_data_types())
    #     print (self.driver.get_performance_data("com.xueqiu.android", "cpuinfo", 5))

    def tearDown(self):
        self.driver.quit()




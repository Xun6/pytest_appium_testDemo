from time import sleep

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.main_page import MainPage


class App:  # 用于启动应用
    driver: WebDriver = None

    @classmethod  # 表示使用类 的方法
    def start(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(15)   #隐式等待

        return MainPage(cls.driver)  # 返回到主页 （应用启动后 会跳转到主页）

    @classmethod
    def quit(cls):  # 退出
        sleep(5)
        cls.driver.quit()

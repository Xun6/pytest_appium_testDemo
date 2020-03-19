# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver



class TestIos:
    def setup(self):
        caps = {}
        caps["platformName"] = "iOS"
        caps["app"] = "/Users/air/Library/Developer/Xcode/DerivedData/UICatalog-gcfqjtbmgufnqjgozehaiwrbmcui/Build/Products/Debug-iphonesimulator/UICatalog.app"
        caps["automationName"] = "XCUITest"
        caps["deviceName"] = "iPhone X"
        caps["platformVersion"] = "12.4"

        self.driver = webdriver.Remote("http://localhost:6723/wd/hub", caps)

    def test_ios_buttons(self):
        el1 = self.driver.find_element_by_accessibility_id("Buttons")
        el1.click()

    def teardown(self):
        sleep(20)
        self.driver.quit()
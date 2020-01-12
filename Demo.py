# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver


caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "mumu"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(8)

el3 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el3.click()

el4 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el4.send_keys("alibaba")

driver.quit()

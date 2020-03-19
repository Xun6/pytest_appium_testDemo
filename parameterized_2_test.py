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
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "android_23"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # caps["unicodeKeyboard"] =True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

        # 显示等待（此方法可以去掉 弹出的 升级提示弹窗）
        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        # )
        # self.driver.find_element_by_id("image_cancel").click()

    def test_parametrize_2_demo_fromtestCasei(self):
        TestCase("testCase.yaml").run(self.driver)  # 调用并运行数据驱动文件
        sleep(2)


    # def test_webview_Demo(self):
    #     self.driver.find_element_by_xpath("//*[@text='交易']").click()
    #     for i in range(5):   # 循环打印五次
    #         sleep(1)
    #         print(self.driver.contexts)   # 打印上下文内容
    #
    #     self.driver.find_element_by_accessibility_id("A股开户").click()
    #     self.driver.switch_to.context(self.driver.contexts.last)  # 切换webview上下文（当找到webview上下文的时候，才可以切换，切换后可以使用css进行定位）
    #     print(self.driver.current_context())  # 打印查看是否切换成功

        # 可借助 chrome://inspect/#devices(工具) 查看当前设备进程开启的 webview调试属性


    def teardown(self):
        self.driver.quit()




#测试步骤采用外部文件驱动
class TestCase:
    def __init__(self, path):   # 初始化方法 读取数据文件
        file=open(path, "r")
        self.steps=yaml.safe_load(file)    # 利用yaml.safe_load 方法读取解析文件，其中steps表示步骤的核心数据（此处先存储一下）

    def run(self, driver: WebDriver):   #传递一个driver（或者全局），并指明类型
        element=None
        for step in self.steps:    # 对步骤中的每一步进行遍历
            if isinstance(step, dict):      # 如果 step 是一个词典，再下一步进行分解
                if "id" in step.keys():      # 对每个词典结构进行解析，此处判断 如果id 存在
                    element=driver.find_element_by_id(step["id"])  # 如果步骤中有id，就获取id查找（此处使用driver，因为上方对象传递了一个webdriver）
                elif "xpath" in step.keys():  # 此处判断如果 xpath 存在
                    element=driver.find_element_by_xpath(step["xpath"])
                else:          # 判断 如果遇到未处理过的表达式，就打印出来
                    print(step.keys())

                if "input" in step.keys():    # 此处判断 如果有 input 交互存在，需要输入 input值
                    element.send_keys(step["input"])
                else:
                    element.click()
                if "get" in step.keys():  # 此处判断 如果有 get 交互存在，需获得get值
                    element.get_attribute(step["get"])


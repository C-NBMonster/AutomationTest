# coding=utf-8

from selenium import webdriver
from AT_Demo.common.logger import Logger
from common.log import Log
import unittest, time


#my_logger = Logger(logger='BaiduTests').getlog()

class BaiduTests(unittest.TestCase):
    def setUp(self):
        self.log = Log("BaiduTests")
        self.driver = webdriver.Firefox()
        print(11)
        self.log.info("打开浏览器")
        print(33)
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"


    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        self.log.info("打开百度首页")
        driver.maximize_window()
        self.log.info("最大化浏览器窗口。")

        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        self.log.info("停顿2秒")
        title = driver.title
        self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()
        self.log.info("关闭并退出浏览器。")

if __name__ == "__main__":
    unittest.main()

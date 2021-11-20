
﻿from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import pprint
address = "https://en.wikipedia.org/wiki/Software_metric"
driver_path = "D:\ПРОГРАММЫ\chromedriver.exe"


class TestResults(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.wait = WebDriverWait(self.driver, 10)
        self.address = address

    def test_open_page(self):
        res = self.driver.get(address)
        print("RESULT", self.driver.current_url, dir(self.driver))
        self.assertIn(self.address, self.driver.current_url)
        script = "return window.performance.getEntries();"
        perf = self.driver.execute_script(script)
        print(perf)
        pprint.pprint(perf)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
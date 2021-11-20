from selenium import webdriver
from selenium.webdriver.support.ui import WebDriveWait
import unittest
address = "https://en.wikipedia.org/wiki/Software_metric"
driver_path = "D:\ПРОГРАММЫ\chromedriver.exe"

class TestResult(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.address = address
    def test_open_page(self):
        res = self.driver.get(address)
        print("RESULT", self.driver.current_url)
        self.assertIn(self.address, self.driver.current_url)

    def tearDown(self):
        self.driver.quit()
if __name__== '__main__':
    unittest.main()
class my_class(object):
    pass




import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver_path = "D:\ПРОГРАММЫ\chromedriver.exe"

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_id("id-search-field")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertFalse("No results found." in driver.page_source)


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()

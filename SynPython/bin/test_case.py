import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class MyTests(unittest.TestCase):
    def setup(self):
        self.browser=webdriver.Chrome()
        print('setup')

    def test_case_1(self):
        b=self.browser
        b.get('http://www.python.org')
        f=b.find_element_by_name('q')
        f.send_keys('python')
        f.send_keys(Keys.RETURN)
    
    def test_case_2(self):
        b=self.browser
        b.get('http://www.python.org')
        f=b.find_element_by_name('q')
        f.send_keys('python')
        f.send_keys(Keys.RETURN)

    def test_case_3(self):
        b=self.browser
        b.get('http://www.python.org')
        f=b.find_element_by_name('q')
        f.send_keys('python')
        f.send_keys(Keys.RETURN)

    def tearDown(self):
        self.browser.close()
        print('tear Down')

unittest.main()

import os
import unittest  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox") 

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),
                                        options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:5000/')
        self.assertEqual(self.browser.title, 'Breaking Melons News')

    def test_navbar(self):
        self.browser.get('http://localhost:5000/')

        btn = self.browser.find_element_by_class('aboutus-link')
        btn.click()
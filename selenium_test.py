import os
import unittest  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from server import app
import server
import time
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox") 

class TestNewsFeed(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),
                                        options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:5000/')
        time.sleep(2)
        self.assertEqual(self.browser.title, 'Breaking Melon News')

    def test_navbar(self):
        self.browser.get('http://localhost:5000/')
        time.sleep(2)
        link = self.browser.find_element_by_class_name('aboutus-link')
        link.click()
        time.sleep(2)
        
        subtitle = self.browser.find_element_by_class_name("subtitle")
        self.assertEqual(subtitle.text, "Chief Melon Analyst")

    def test_carousel_link(self):
        self.browser.get('http://localhost:5000/')
        time.sleep(2)
        link = self.browser.find_element_by_class_name('carousel-link')
        link.click()
        time.sleep(2)

        author = self.browser.find_element_by_class_name("autor-article")
        self.assertEqual(author.text, "Mel Melitpolski")

    def test_hover(self):
        self.browser.get('http://localhost:5000/')
        time.sleep(2)
        a = ActionChains(self.browser)
        card = self.browser.find_element_by_class_name('news-card')
        a.move_to_element(card).perform()
        time.sleep(2)

        visible_melons = self.browser.find_elements_by_class_name("card-visible")
        self.assertEqual(len(visible_melons), 1) 
        melon_link = self.browser.find_element_by_css_selector('.card-visible .card-link')
        melon_link.click()
        time.sleep(2)
        self.assertNotIn(self.browser.current_url, 'http://localhost:5000/' )
    

if __name__ == "__main__":
    unittest.main()
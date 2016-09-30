from selenium import webdriver
import unittest

class VisitIndexTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)
    
    def tearDown(self):
        self.browser.quit()

    def test_visit_index_page(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("Imaginary Beasts", self.browser.title)

if __name__ == '__main__':
    unittest.main()


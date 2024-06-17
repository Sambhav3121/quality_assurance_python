import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestRotateImageE2E(unittest.TestCase):
    def setUp(self):
        chromedriver_path = 'C:\\Users\\sambhav_\\OneDrive\\Escritorio\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
        brave_path = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

        options = Options()
        options.binary_location = brave_path

        self.driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

    def test_rotate_3x3(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        input_field = driver.find_element(By.ID, "matrix")
        submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

        input_field.send_keys("1,2,3;4,5,6;7,8,9")
        submit_button.click()

        result = driver.find_element(By.TAG_NAME, 'h2').text
        self.assertIn("Result: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]", result)

    def test_rotate_4x4(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        input_field = driver.find_element(By.ID, "matrix")
        submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

        input_field.send_keys("5,1,9,11;2,4,8,10;13,3,6,7;15,14,12,16")
        submit_button.click()

        result = driver.find_element(By.TAG_NAME, 'h2').text
        self.assertIn("Result: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]", result)

    def test_invalid_input(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        input_field = driver.find_element(By.ID, "matrix")
        submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

        input_field.send_keys("")
        submit_button.click()

        error = driver.find_element(By.TAG_NAME, 'h2').text
        self.assertIn("ValueError: Matrix input cannot be empty", error)

    def test_mixed_non_integer_input(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")

        input_field = driver.find_element(By.ID, "matrix")
        submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

        input_field.send_keys("1,2,3;4,a,6;7,8,9")
        submit_button.click()

        error = driver.find_element(By.TAG_NAME, 'h2').text
        self.assertIn("ValueError", error)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

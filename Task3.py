import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

class SauceDemoLoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Optional: Run in headless mode
        service = Service(r"C:\Chromedriver\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # Update path if needed
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def test_valid_login(self):
        self.login("standard_user", "secret_sauce")
        self.assertIn("inventory", self.driver.current_url)

    def test_invalid_login(self):
        self.login("invalid_user", "wrong_pass")
        error = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Username and password do not match", error)

    def test_empty_username(self):
        self.login("", "secret_sauce")
        error = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Username is required", error)

    def test_empty_password(self):
        self.login("standard_user", "")
        error = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Password is required", error)

    def test_empty_fields(self):
        self.login("", "")
        error = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Username is required", error)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

from selenium import webdriver
import os
from selenium.webdriver.common.by import By


class LoginTests():

   def test_validLogin(self):
       baseURL = "https://letskodeit.teachable.com/"
       driverLocation = "/Users/mdrubel/Documents/workspace_python/letsKodeit/chromedriver"
       os.environ["webdriver.chrome.driver"] = driverLocation
       # Instantiate Chrome Browser Command
       driver = webdriver.Chrome(driverLocation)
       driver.maximize_window()
       driver.implicitly_wait(3)
       driver.get(baseURL)
       loginLink = driver.find_element(By.LINK_TEXT, "Login")
       loginLink.click()

       emailField = driver.find_element(By.ID, "user_email")
       emailField.send_keys("test@email.com")

       passwordField = driver.find_element(By.ID, "user_password")
       passwordField.send_keys("abcabc")

       loginButton = driver.find_element(By.NAME, "commit")
       loginButton.click()


ff = LoginTests()
ff.test_validLogin()
